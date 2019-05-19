# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:18:07 2019
pip 
@author: Manjot
"""

import time
start = int(round(time.time()))

t1 = int(round(time.time()))

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "C:/Users/Manjot/Desktop/SPSS_Complex_Samples_22.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

print(recognized_text)

end = int(round(time.time()))

print(end-start)
