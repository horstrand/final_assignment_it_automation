#!/usr/bin/env python3

import requests
import os

# This script uploads files using the python request

url = "http://localhost/upload/"
input_dir=os.path.join(os.path.expanduser('~'),'supplier-data/images')

for image_file in os.listdir():
	im_file_total = os.path.join(input_dir, image_file)
	with open(im_file_total, 'rb') as im_opened:
		r = requests.post(url, files={'file': im_opened})