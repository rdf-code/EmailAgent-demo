from openai import OpenAI

class AiAgent:
    def __init__(self):
        self.client = OpenAI()

    def generate_chatgpt_response(self, email_content):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ești un agent de customer service care raspunde la email într-o manieră politicoasă și care încearcă să ajute cum poate, la final trebuie sa inchei conversatia intr-un mod formal din partea echipei GoCamper."},
                {"role": "user", "content": email_content}
            ]
        )
        return completion.choices[0].message
