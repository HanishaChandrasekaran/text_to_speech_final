import pytesseract
import cv2

# Uncomment and set this if using Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    try:
        image = cv2.imread(image_path)
        return pytesseract.image_to_string(image)
    except Exception as e:
        print("Error reading image:", e)
        return ""
