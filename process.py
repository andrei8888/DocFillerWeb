from difflib import SequenceMatcher

from pytesseract.pytesseract import Output
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'


def open_and_preproc(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return img


SPCLEP = "SPCLEP"
SIM_ROMANIA = "ROMANIA"
SIM_ROUMANIE = "ROUMANIE"


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def crop_to_infos(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['level'])
    x_info1 = 0
    y_info1 = 0
    x_info2 = 0
    y_info3 = 0
    for i in range(n_boxes):
        text = d['text'][i]
        if similar(text, SIM_ROUMANIE) > 0.8:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            x_info1 = x + w
            y_info1 = y + h
        if similar(text, SIM_ROMANIA) > 0.8:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            x_info2 = x + w
        if similar(text, SPCLEP) > 0.8:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            y_info3 = y + h + 20
    if y_info3 < y_info1:
        y_info3 = img.shape[0]
    img = img[y_info1:y_info3, x_info1:x_info2]
    return img


def resize_with_scale(img, scale):
    scale_percent = scale
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img
