# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:07:52
# @Last Modified by:   amish
# @Last Modified time: 2021-03-01 12:07:12

from difflib import SequenceMatcher
import sys

def get_name(text, words, email):
	try:
		fullname = ""
		for i in email:
			if i == '@':
				break
			fullname += i

		vect = []
		for i in words:
			vect.append([i, SequenceMatcher(None, fullname.strip().lower(), i.strip().lower()).ratio()])

		first = last = mid = None
		names =  sorted(vect, reverse = True, key = lambda x: x[1])[0][0]

		vect = []
		for i in text.split("\n"):
			vect.append([i, SequenceMatcher(None, fullname.strip().lower(), i.strip().lower()).ratio()])

		vect = sorted(vect, reverse = True, key = lambda x: x[1])
		names = vect[0][0]
		v = []
		for name in names.split():
			v.append([name, SequenceMatcher(None, fullname.strip().lower(), name.strip().lower()).ratio()])

		temp = ""
		for li in v:
			if li[1] >= 0.20:
				temp += li[0]
				temp += " "
		names = temp[:]
		if names[-1] == ' ':
			names = names[:]

		if len(names) >= 1:
			for i in range(len(names)-1, 0, -1):
				if names[i] in (',', ' ', ':', ';', '.'):
					continue
				else:
					names = names[0:i+1]
					break
			# Removing from text
			for name in names.split():        
				if name in text:
					text = text.replace(name, "")
			# Removing from words
			temp = words.copy()
			for i in range(0, len(words)):
				sentence = words[i]
				for word in sentence.split():
					for name in names.split():
						if word.strip().lower() == name.strip().lower():
							sentence = sentence.replace(name, "")
				temp[i] = sentence
			words = temp.copy()
		else:
			names = fullname
		return [text, words, names]
	except:
		# print(sys.exc_info()[1])
		f = ""
		if email != None:
			for i in email:
				if i == '@':
					break
				f += i
		return [text, words, f]