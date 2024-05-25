"Grab the whole screen"

import pyscreenshot as ImageGrab
import easyocr

# grab fullscreen
im = ImageGrab.grab()

# save image file
#im.save("fullscreen2.png")
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    print(pytesseract.image_to_string('fullscreen2.png', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('fullscreen2.png', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass