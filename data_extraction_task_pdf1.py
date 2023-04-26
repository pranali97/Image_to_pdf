from pytesseract import image_to_string
from pdf2image import convert_from_path
import cv2
import numpy as np
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

path_to_pdf = "All Files/pre_2.pdf"
final_image_text = get_text_from_pdf(path_to_pdf)

# preprocess image with computer vision 
def preprocess_image(img):
    """text is not extracted properly as there is shadow present in image to fix that we have to 
        Use Computer Vision to clean the image"""
    grey_scale = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # print(grey_scale.shape)
    resized_image = cv2.resize(grey_scale, None, fx=1.5, fy=1.5)   #cv.INTER_LINEAR is used for zooming
    cv2.imshow('path_to_pdf',resized_image)
    # print(imag1)
    processed_image = cv2.adaptiveThreshold(
    resized_image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 65, 15
    )
    return processed_image

out_img = preprocess_image(convert_pdf_to_img(path_to_pdf)[0])
result = convert_image_to_text(out_img)
# print(result)

# Using Regex extracted keyword information Name, date  
Name_and_date = "Name:(.*)"
Name_date_matches = re.findall(Name_and_date,result)
print("Name:",Name_date_matches[0])





        