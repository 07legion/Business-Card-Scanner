# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:07:39
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-05-10 11:09:33

import sys, re
from modules import glob

def get_website(text, words, email_list):
	try:
		w = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", text)
		website_list = []
		for i in w:
			website_list.append(i[0])
		## Removing Email
		# Removing from text
		for email  in email_list:
			if email in text:
				text = text.replace(email, "")
		for email in glob.ema:	
			if email in text:
				text = text.replace(email, "")
		# Removing from words[]
		temp = words.copy()
		for email in email_list:
			for sentence in words:
				if email in sentence:
					temp.remove(sentence)
					break
		words = temp.copy()
		
		## Removing Website
		# Removing from text
		for website in website_list:
			if website in text:
				text = text.replace(website, "")
		for website in glob.web:
			if website in text:
				text = text.replace(website, "")

		# Removing from words[]
		temp = words.copy()
		for i in range(0, len(words)):
			sentence = words[i]
			for word in sentence.split():
				for web in website_list:
					if web.strip().lower() == word.strip().lower():
						sentence = sentence.replace(word, "")
			temp[i] = sentence
		words = temp.copy()
		website_list = list(map(lambda x: x.strip().lower(), website_list))
		return [text, words, website_list]
	except:
		# print(sys.exc_info()[1])
		# print("Cannot extract website!!")
		return [text, words, ""]