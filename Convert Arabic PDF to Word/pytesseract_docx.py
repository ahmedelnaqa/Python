import os
from docx import Document
from PIL import Image
import pytesseract
# Create a new Document

#--------------------------------------------------
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.__version__)

# arabic text image to string
#print(pytesseract.image_to_string(Image.open('pages/one/v9xf74ok_Page_003.png'), lang='ara'))

ImagefilesPath= "C:\\Users\\Samir\\PycharmProjects\\email\\pages"

Image_files = [f for f in os.listdir(ImagefilesPath) if f.endswith('.jpg')]
Image_files.sort()  # Optional: sort files if needed

for index, image_file in enumerate(Image_files):
    image_path = os.path.join(ImagefilesPath, image_file)
    print(image_path)
    #               pytesseract.image_to_string(Image.open('pages/one/v9xf74ok_Page_003.png'), lang='ara'))
    ExtractedDate = pytesseract.image_to_string(Image.open(image_path), lang='ara')

    # Add a paragraph
    doc = Document()
    doc.add_paragraph(ExtractedDate)

    # Save the document
    #file_path = f'C:\\Users\\Samir\\PycharmProjects\\email\\OutPutDocx\\{file_name}.{file_extension}'
    file_path = f'C:\\Users\\Samir\\PycharmProjects\\email\\OutPutDocx\\{image_file}.docx'
    doc.save(file_path)

    print(file_path)
    ExtractedDate=""
