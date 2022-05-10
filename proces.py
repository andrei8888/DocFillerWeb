import numpy as np
from PIL import Image
from pytesseract.pytesseract import Output
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'

img = cv2.imread('C:/Users/andrei/Documents/licenta/resources_lic/smn.jpg', cv2.IMREAD_GRAYSCALE)
th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("s", th)  #
print(pytesseract.image_to_string(img, lang='ron'))
cv2.waitKey(0)
# print(pytesseract.image_to_boxes(img))
# print(pytesseract.image_to_data(img))
# print(pytesseract.image_to_osd(img))
