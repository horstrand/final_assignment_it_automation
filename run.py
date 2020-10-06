#! /usr/bin/env python3

import os
import requests

url = "http://35.239.174.19/fruits/"
input_dir=os.path.join(os.path.expanduser('~'),'supplier-data/descriptions')

for desc_file in os.listdir(input_dir):
	if 'txt' in desc_file:
		file_total = os.path.join(input_dir, desc_file)
		data = {}
		with open(file_total, 'rb') as opened:
			data['name'] = opened.readline().decode("utf-8").strip()
			data['weight'] = int(opened.readline().decode("utf-8").strip().split()[0])
			data['description'] = opened.readline().decode("utf-8").strip()
			data['image_name'] = os.path.splitext(desc_file)[0] + '.jpeg'
		r = requests.post(url, data=data)
		#print(data)
		print(r.status_code)
