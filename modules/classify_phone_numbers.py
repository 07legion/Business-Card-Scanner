# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:08:52
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-03-03 10:56:34

import sys
import phonenumbers
from modules import glob

def get_phone_numbers(text, words):
	try:
		numbers = phonenumbers.PhoneNumberMatcher(text, "IN") 
		phone_numbers = []
		for match in numbers:
			n = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
			phone_numbers.append([n, match.start, match.end])
		numbers = phonenumbers.PhoneNumberMatcher(text, "IN") 
		phone_numbers = []
		for match in numbers:
			n = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
			phone_numbers.append([n, match.start, match.end])

		flag = 0; r = []; m = d = f = o = ""
		for li in phone_numbers:
			phone = li[0]; start = li[1]; end = li[2]
			s = ""; 
			for i in range(start-1, 0, -1):
				if text[i] in glob.punctuation:
					continue
				s = text[i] + s
				if s.strip().lower() in glob.mobiles:
					m = phone; flag = 1
					r.append([s, m])
					break
				if s.strip().lower() in glob.offices:                    
					o = phone; flag = 1
					r.append([s, o])
					break
				if s.strip().lower() in glob.fax:
					f = phone; flag = 1
					r.append([s, f])
					break
				if s.strip().lower() in glob.direct:
					d = phone; flag = 1
					r.append([s, d])
					# print(s, phone)
					break

		if flag == 0 and len(phone_numbers) > 0:
			m = phone_numbers[0][0]
			text = text.replace(m, "")
			temp = words.copy()
			for i in words:
				for j in (i.split()):
					if j == m:
						temp.remove(i) 
						break
			words = temp.copy()
		else:
			for li in r:
				if li[0] in text:
					text = text.replace(li[0], "")
				if li[1] in text:
					text = text.replace(li[1], "")
				temp = words.copy()
				for sentence in words:
					for word in (sentence.split()):
						if word == li[1]:
							temp.remove(sentence) 
							break
				words = temp.copy()
		return [text, words, [o, m, d, f]]
	except:
		# print(sys.exc_info()[1])
		return [text, words, [None, None, None, None]]