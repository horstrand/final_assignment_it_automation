#!/usr/bin/env python3

import os
from PIL import Image

input_dir=os.path.join(os.path.expanduser('~'),'supplier-data/images')

for image_file in os.listdir(input_dir):
	if 'tiff' in image_file:
		file, ext = os.path.splitext(image_file)
		im_file_total = os.path.join(input_dir, file)
		im = Image.open(im_file_total+ext)
		im.convert("RGB").resize((600,400)).save(im_file_total + '.jpeg')
