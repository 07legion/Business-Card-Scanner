# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:08:09
# @Last Modified by:   amish
# @Last Modified time: 2021-03-01 12:16:46

from difflib import SequenceMatcher
import sys
from modules import read

def get_designation(text, words):
	try:
		designations = read.read_file("designations.txt")
		departments = read.read_file("departments.txt")
		vect1 = []
		for designation in designations:
			for word in words:
				similarity_ratio = SequenceMatcher(None, word.lower(), designation.lower()).ratio()
				vect1.append([similarity_ratio, [word, designation]])    
		vect1 = sorted(vect1, reverse = True)
		vect2 = []
		for department in departments:
			for word in words:
				similarity_ratio = SequenceMatcher(None, word.lower(), department.lower()).ratio()
				vect2.append([similarity_ratio, [word, department]])
		vect2 = sorted(vect2, reverse = True)
		designation1 = designation2 = ""
		if vect1[0][0] >= 0.7:
			designation1 = vect1[0][1][0]
		designation1 = vect1[0][1][0]
		if vect2[0][0] >= 0.7 and designation1 != vect2[0][1][0]:
			designation2 = vect2[0][1][0]
		# Removing from text desig1
		if designation1 in text:
			text =  text.replace(designation1, "")
		# Removing from words desig1
		if designation1 in words:
			words.remove(designation1)
		# Removing from text desig2
		if designation2 in text:
			text =  text.replace(designation2, "")
		# Removing from words desig2
		if designation2 in words:
			words.remove(designation2)
		
		if (designation1.strip().lower() == designation2.strip().lower()) and designation1.strip() != "":
			return [text, words, designation1]
		else:
			return [text, words, str(designation1 + " " + designation2)]
	except:
		# print("Cannot extract designation!!")
		# print(sys.exc_info()[1])
		return [text, words, ""]
