# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:34:20
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-03-03 10:53:44


# text = ""; words  = []

image_path = "./uploaded_images"
file_path = "./files"

v = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 
     0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 
     0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 
     0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 
     0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89]

ema = ['e-mail','e-mail:', 'e-mail-' 'e-mail:-','e-mail.:', 'email:', 'email', 'mail', 'mail.:', 'mail:', 'mail:-', 'mail -', 'mail-']

web = ["web.", "web", "web:", "web:.", "web-","web:-","web -", "website", "website.", "website:", "website:.", "websit-", "website:-", "website -"]

offices = ['Office', 'office', 'Off', 'O', 'Telephone' 'Tel', 'tele', 'tel', 'T', 'o', 'off', 'telephone', 'tel:.', 'tel.', 'tel-']
mobiles = ['Mobile', 'mobile', 'Mob', 'Cell', '(M)','M', 'm', 'cell', '(m)', 'mob', 'mob.', 'mobile:', 'mobile:.', 'mobile-']
direct = ['Direct', 'direct', 'Dir', 'dir', 'directdial', 'Direct Dial', 'direct dial', 'Dial', 'dial', 'Main' ,'D', 'toll free', 'direct', 'Phone', 'phone', 'd']
fax = ['Fax', 'fax', 'FAX', 'F:', '(F)', 'Fax', 'F', 'f', 'f:', '(f)']
punctuation = ['.', ':', '-', ';', ' ', '--', '---', '::', '..', '...', ':-', '|', '/', '',
				'>', '<', '?', '\\', '  ', '(', ')', ',', '!']
