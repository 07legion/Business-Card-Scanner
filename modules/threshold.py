# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:05:52
# @Last Modified by:   amish
# @Last Modified time: 2021-03-01 11:56:50

import cv2
import sys

def threshold_image(img):
	try:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (5,5),0)
		ret3, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		return thresh
	except:
		# print("Cannot threshold the image!!")
		# print(sys.exc_info()[1])
		return None