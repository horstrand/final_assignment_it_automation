#!/usr/bin/env python3

import os
from PIL import Image

input_dir=os.path.join(os.path.expanduser('~'),'supplier-data/images')

for image_file in os.listdir():
	im_file_total = os.path.join(input_dir, image_file)
	im = Image.open(im_file_total)
	im.convert("RGB").resize((640,480)).save(im_file_total, 'JPEG')