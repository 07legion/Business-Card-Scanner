# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:07:19
# @Last Modified by:   amish
# @Last Modified time: 2021-03-01 12:07:17

import re, sys

def get_email(text):
	try:
		email_list = re.findall(r"[A-Za-z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", text)
		email_list = list(map(lambda x: x.strip().lower(), email_list))
		return email_list
	except:
		# print(sys.exc_info()[1])
		# print("Cannot extract email!!")
		return None