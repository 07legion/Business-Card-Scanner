# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:06:11
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-03-03 10:56:12

from string import ascii_lowercase, ascii_uppercase, digits
import sys
from modules import information, read

def clean_all(txt):
	temp = [ascii_lowercase, ascii_uppercase, digits]
	txt2 = txt
	for ch in txt:
		if ch in ascii_lowercase or ch in ascii_uppercase or ch in digits:
			continue
		else:
			txt2 = txt2.replace(ch, " ")
	txt = txt2[:]
	return txt

def clean_text(text):
	try:
		ctry = cit = ""
		cities = read.read_file("worldcities.csv"); countries = read.read_file("countries.txt")
		countries = list(map(lambda x: x.strip().lower(), countries))
		cities = list(map(lambda x: x.strip().lower(), cities))
		txt = clean_all(text) 
		for word in txt.split():
			if word.lower() in countries:
				ctry = word
				if word in text.split(): 
					text.replace(word, "")

		for word in txt.split():
			if word.lower() in cities:
				cit = word
				if word in text.split(): 
					text.replace(word, "")

		text2 = ""
		for i in range(0, len(text)):
			if text[i] == ' ' or text[i] == '-':
				j = i; ct1 = ct2 = 0; j -= 1
				while j >= 0 and (text[j] >= '0' and text[j] <= '9'):
					j -= 1; ct1 += 1
				j = i; j += 1
				while j < len(text) and (text[j] >= '0' and text[j] <= '9'):
					j += 1; ct2 += 1
				if ct1 >= 2 and ct2 >= 2:
					continue
				else:
					text2 += text[i]
			else:
				text2 += text[i]
		text = text2[:]

		text2 = text[:]
		for ch in text:
			if ch in ['`', '~', '#', '*', '^', '$', '%']:
				text2 = text.replace(ch, "")
		text = text2[:]
		return [text, ctry, cit]
	except:
		# print("Text can't be cleaned!!\n")
		# print(sys.exc_info()[1])
		return [text, "", ""]

def clean_words(text):
	try:
		words = text.split("\n")
		temp = words.copy()
		for sentence in words:
			if information.info(sentence) < 5:
				temp.remove(sentence)
		words = temp.copy()
		return words
	except:
		# print("Words cannot be cleaned!!\n")
		# print(sys.exc_info()[1])
		return []
