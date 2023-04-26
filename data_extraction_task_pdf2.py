from pytesseract import image_to_string
from pdf2image import convert_from_path
import re

def convert_pdf_to_img(pdf_file):
    """Converting pdf to image"""
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    """With pytesseract converting image to string"""
    text = image_to_string(file)
    return text

def get_text_from_pdf(pdf_file):
    """Getting text data from pdf image"""
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)
    return final_text

path_to_pdf = "All Files/pd_2.pdf"
text = get_text_from_pdf(path_to_pdf)
print(text)

# Using Regular Expression extracted relevent information from text
patient_information = "Patient Information(.*?)\(\d{3}\)"
birth_date = "((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)"
policy_num = "\d{10}"
expiry_date = '\d{2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}'

patient_info_matches = re.findall(patient_information,text,flags = re.DOTALL) 
birth_date_matches = re.findall(birth_date,text)
policy_num_matches = re.findall(policy_num,text)
expiry_date_matches = re.findall(expiry_date,text)

print("patient name:-",patient_info_matches[0])
print("Birth date:- ",birth_date_matches[0][0])
print("policy_number:-",policy_num_matches[0])
print("Expiry_date:-",expiry_date_matches[0])

