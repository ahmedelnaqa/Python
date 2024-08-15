import os
from PIL import Image
import pytesseract
from docx import newdocument

# Set the path to the Tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Directory containing the images
image_dir = 'pages/one'  # Update this to your image directory
log_file_path = 'processed_images_log.txt'
output_doc_path = 'output_document.docx'

# Create a new Word document
doc = newdocument()

# Create or open the log file
with open(log_file_path, 'a') as log_file:
    # Loop through all files in the image directory
    for filename in os.listdir(image_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.tiff')):
            image_path = os.path.join(image_dir, filename)

            # Perform OCR on the image
            try:
                text = pytesseract.image_to_string(Image.open(image_path), lang='ara')

                # Append the text to the Word document
                doc.add_heading(filename, level=1)
                doc.add_paragraph(text)

                # Log the processed image filename
                log_file.write(f'{filename}\n')

                print(f'Processed: {filename}')

            except Exception as e:
                print(f'Error processing {filename}: {e}')

# Save the Word document
doc.save(output_doc_path)

print(f'OCR completed. Output saved to {output_doc_path}. Log saved to {log_file_path}.')
