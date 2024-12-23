import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from APIAgents.OpenAI_Agent import AiAgent

# Define the worker thread for making API calls without freezing the UI
class ApiThread(QThread):
    response_signal = pyqtSignal(str)

    def __init__(self, email_content):
        super().__init__()
        self.email_content = email_content

    def run(self):
        agent = AiAgent()
        response = agent.generate_chatgpt_response(self.email_content)
        # Ensure you are emitting the string response correctly
        self.response_signal.emit(response)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('OpenAI ChatGPT Integration')
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        
        self.inputField = QTextEdit()
        self.inputField.setPlaceholderText("Enter your email content here...")
        layout.addWidget(self.inputField)
        
        self.sendButton = QPushButton('Send')
        self.sendButton.clicked.connect(self.onSend)
        layout.addWidget(self.sendButton)
        
        # Label as a loading indicator
        self.loadingLabel = QLabel('')
        layout.addWidget(self.loadingLabel)
        
        self.responseField = QTextEdit()
        self.responseField.setReadOnly(True)
        layout.addWidget(self.responseField)
        
        self.copyButton = QPushButton('Copy to Clipboard')
        self.copyButton.clicked.connect(self.onCopy)
        layout.addWidget(self.copyButton)
        
        self.setLayout(layout)

    def onSend(self):
        email_content = self.inputField.toPlainText()  # Use toPlainText for QTextEdit
        if email_content.strip():  # Check for non-empty content
            self.sendButton.setDisabled(True)  # Disable the send button
            self.loadingLabel.setText("Loading response...")
            self.thread = ApiThread(email_content)
            self.thread.response_signal.connect(self.onResponse)
            self.thread.start()
        else:
            self.loadingLabel.setText("Please enter some content before sending.")

    def onResponse(self, response):
        self.responseField.setText(response)
        self.sendButton.setEnabled(True)  # Re-enable the send button
        self.loadingLabel.setText("")  # Remove loading text

    def onCopy(self):
        QApplication.clipboard().setText(self.responseField.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
