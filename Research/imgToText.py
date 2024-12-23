from PIL import Image
import pytesseract

value = 5
# Path to the image you want to process
image_path = f"C:\\Users\\dm\\Desktop\\poze ci\\{value}.png"

# Open the image using Pillow
image = Image.open(image_path)

# Convert image to grayscale
image = image.convert('L')
image.save("img.png")
# Preprocess image here (denoise, threshold, etc.) if necessary

# Set tesseract to use the Romanian language pack
# OEM 1 means using LSTM only, which is good for image-only OCR
# PSM 11 is for sparse text with good OCR accuracy
custom_oem_psm_config = r'--oem 1 --psm 11 -l ron'

# Use PyTesseract to do OCR on the image
text = pytesseract.image_to_string(image, config=custom_oem_psm_config)

# Print the text
print(text)
