# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:05:31
# @Last Modified by:   amish
# @Last Modified time: 2021-03-02 09:26:17

import os, sys
import cv2
import pandas as pd
from modules import glob

def read_image(s):
	try:
		path = os.path.join(glob.image_path, s)
		img = cv2.imread(path)
		return img
	except:
		# print(sys.exc_info()[1])
		# print("Image Can't be loaded!!")
		return None

def read_file(s):
	try:
		path = os.path.join(glob.file_path, s)
		if s == "worldcities.csv":
			df = pd.read_csv(path)["city_ascii"]
			return list(df)
		with open(path) as f:
			li = f.readlines()
		li = list(set([x.strip() for x in li]))
		if '' in li:
			li.remove('')
		return li
	except:
		# print("File can't be loaded!!")
		# print(sys.exc_info()[1])
		return []