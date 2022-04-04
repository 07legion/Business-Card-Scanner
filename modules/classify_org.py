# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:07:32
# @Last Modified by:   amish
# @Last Modified time: 2021-03-01 11:54:24

import sys

def get_organization(email):
	try:
		org = email.split("@")[1].split(".")[0].upper()
		org = org.upper()
		return org
	except:
		# print(sys.exc_info()[1])
		# print("Cannot extract organization!!")
		return ""