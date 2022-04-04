# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:09:17
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-05-08 17:31:03

import re, sys
from modules import glob
import postal 
from postal.parser import parse_address

def get_address(text, words, li, ctry, cit):
	try:
		address = ""
		for i in words:
			address += i
			address += ' '
		tup = parse_address(address)
		zipcode = state = country = city = None
		c1 = ct1 = s1 = z1 = None
		for i in tup:
			if i[1] == 'postcode':
				text = text.replace(i[0], "")
				zipcode = i[0]
				z1 = i[0].capitalize()
			elif i[1] == 'city':
				text = text.replace(i[0], "")
				city = i[0]
				c1 = i[0].capitalize()
			elif i[1] == 'state':
				text = text.replace(i[0], "")
				state = i[0]
				s1 = i[0].capitalize()
			elif i[1] == 'country':
				text = text.replace(i[0], "")
				country = i[0]
				ct1 = i[0].capitalize()

		if country != None:
			index = address.lower().find(country.lower())
			address = address[0:index]
			for i in range(len(address)-1, 0, -1):
				if address[i] in (',', ' ', ':', ';', '.'):
					continue
				else:
					address = address[0:i+1]
					break
			country = country.capitalize()
		if state != None:
			index = address.lower().find(state.lower())
			address = address[0:index]
			for i in range(len(address)-1, 0, -1):
				if address[i] in (',', ' ', ':', ';', '.'):
					continue
				else:
					address = address[0:i+1]
					break
			state = state.capitalize()
		if city != None:
			index = address.lower().find(city.lower())
			address = address[0:index]
			for i in range(len(address)-1, 0, -1):
				if address[i] in (',', ' ', ':', ';', '.'):
					continue
				else:
					address = address[0:i+1]
					break
			city = city.capitalize()
			if address[-1] == ',' or address[-1] == ' ':
				address = address[0:index-1]
		address = address.strip()

		email_list = li[0]; org = li[1]; web_list = li[2]; 
		names = li[3]; designation = li[4]; phone = li[5]; name = []
		if names != None:
			name = names.split()
		else:
			name.append('')
		email_list = [i for i in email_list if i] 
		web_list = [i for i in web_list if i] 
		phone = [i for i in phone if i] 
		name = list(map(lambda x: x.strip().lower(), name))
		email_list = list(map(lambda x: x.strip().lower(), email_list))
		web_list = list(map(lambda x: x.strip().lower(), web_list))
		phone = list(map(lambda x: x.strip().lower(), phone))
		offices = list(map(lambda x: x.strip().lower(), glob.offices))
		mobiles = list(map(lambda x: x.strip().lower(), glob.mobiles))
		fax = list(map(lambda x: x.strip().lower(), glob.fax))
		direct = list(map(lambda x: x.strip().lower(), glob.direct))
		temp = address[:]; 
		for i in address.split():
			if (i.lower() in name) or (i.lower() in email_list) or (i.lower() in web_list) or (i.lower() in phone) or (i.lower() in offices) or (i.lower() in fax) or (i.lower() in mobiles) or (i.lower() in direct):
				temp = temp.replace(i, '')

			if i.lower() in glob.punctuation:
				temp = temp.replace(i, '')
		numbers = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", address)
		numbers.extend(["+91", "+77", "+1", "ph.", "Ph.", "ph", "Ph", "Mo.", "mo.", "(O)"]) # To remove these prefixes from the text
		for i in numbers:
			if i in address:
				temp = temp.replace(i, "")
		address = temp[:]

		## City
		if cit != None: city = cit.capitalize()
		## Country
		if ct1 == None and ctry != None: ct1 = ctry.capitalize()
		return [address, z1, c1, s1, ct1]; 
	except:
		# print(sys.exc_info()[1])
		# print("Cannot extract address!!")
		return [None, None, None, None, None]