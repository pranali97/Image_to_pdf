import pytesseract
from pdf2image import convert_from_path
# import pdf2image
pdfs = "/home/pranalif/Desktop/image_to_text/All Files/pd_2.pdf"

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path,1)
    for pageNum, imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob)
        with open(f"{pdf_path}_page_{pageNum}.txt",'w') as the_file:
            the_file.write(text)



