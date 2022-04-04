# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-03-01 09:37:05
# @Last Modified by:   amish
# @Last Modified time: 2021-03-02 15:32:06

from modules import extract, read, threshold, image_processing, clean, glob
from modules import classify_email, classify_org, classify_website, classify_name
from modules import classify_designation, classify_phone_numbers, classify_address 

def main_func(filename):
	img = read.read_image(filename)
	processed_image = image_processing.process_image(img)
	text = extract.extract_text(processed_image)
	text, country, city = clean.clean_text(text); words = clean.clean_words(text)
	li = []
	email_list = classify_email.get_email(text); 
	li.append(email_list)
	if len(email_list) > 0:
		org = classify_org.get_organization(email_list[0]); li.append(org)
	else: org = None; li.append(None)
	text, words, web_list = classify_website.get_website(text, words, email_list)
	li.append(web_list)
	if len(email_list) > 0:
		if len(email_list) >= 2:
			text, words, name = classify_name.get_name(text, words, email_list[1])
		else:
			text, words, name = classify_name.get_name(text, words, email_list[0])
		li.append(name)
	else: 
		name = None; li.append(None)
	text, words, desig = classify_designation.get_designation(text, words)
	li.append(desig)
	text, words, phone = classify_phone_numbers.get_phone_numbers(text, words); li.append(phone)
	address = classify_address.get_address(text, words, li, country, city)
	text = ""; words = [] 
	return [email_list, org, web_list, name, desig, phone, address]