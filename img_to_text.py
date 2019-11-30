'''need to install opencv-python 
pip install opencv-python
need to install tesseract-ocr setup
https://github.com/UB-Mannheim/tesseract/wiki(tesseract-ocr-w64-setup-v5.0.0-alpha.20191030.exe)
'''
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
image = cv2.imread('image_path')  
text = pytesseract.image_to_string(image)
print(text)
