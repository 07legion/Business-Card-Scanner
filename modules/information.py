# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:04:30
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-05-08 17:14:28

import sys
from string import ascii_lowercase, ascii_uppercase, digits 

def info(txt):
	try:
		ct = 0; eng_alphabets = ascii_lowercase + ascii_uppercase + digits
		for ch in txt:
			if ch in eng_alphabets:
				ct += 1
		return ct
	except:
		# print("Cannot find information from the text!!")
		# print(sys.exc_info()[1])
		return None