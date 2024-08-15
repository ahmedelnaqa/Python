from PIL import Image

import pytesseract


print(pytesseract.__version__)

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
#print(pytesseract.image_to_string(Image.open('textarabic.png')))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
#print(pytesseract.image_to_string('textarabic.png'))

# List of available languages
#print(pytesseract.get_languages(config=''))

# French text image to string
print(pytesseract.image_to_string(Image.open('pages/one/v9xf74ok_pages-to-jpg-0014.jpg'), lang='ara'))






