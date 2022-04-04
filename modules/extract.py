# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:06:25
# @Last Modified by:   amish
# @Last Modified time: 2021-02-27 17:35:05


import pytesseract
def extract_text(img):
	try:
		return (pytesseract.image_to_string(img))
	except:
		return ""