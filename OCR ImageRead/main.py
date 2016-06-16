from pytesseract import image_to_string
import pytesseract
import tesseract
#import Image
from PIL import Image
image =Image.open('test.tiff')
im = image_to_string(image)

