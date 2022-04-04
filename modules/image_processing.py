# -*- coding: utf-8 -*-
# @Author: amish
# @Date:   2021-02-27 17:04:59
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-05-08 17:13:57

import pytesseract
import re, cv2, math
import numpy as np
from scipy import ndimage
from imutils.perspective import four_point_transform
from modules import glob, threshold, information

def check_orientation(img):
	newdata = pytesseract.image_to_osd(np.array(img))
	orgi_confidence = int(re.search('(?<=Orientation confidence: )\d+', newdata).group(0))
	if orgi_confidence > 0:
		return rotate(img)
	else:
		return img


def rotate(image, center=None, scale=1.0):
	angle = 360 - int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
	(h, w) = image.shape[:2]

	if center is None:
		center = (w / 2, h / 2)
	mmm = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, mmm, (w, h))
	return rotated

def process_image (img):
	thresh = threshold.threshold_image(img)
	edgeImg = np.asarray(thresh, np.uint8)
	orig = img.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_edges = cv2.Canny(gray, 100, 100, apertureSize=3)

	contours, heirarchy = cv2.findContours(edgeImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	level1 = []

	for i, tupl in enumerate(heirarchy[0]):
		if tupl[3] == -1:
			tupl = np.insert(tupl, 0, [i])
			level1.append(tupl)
	significant = []
	tooSmall = edgeImg.size * 5 / 100
	for tupl in level1:
		contour = contours[tupl[0]];
		area = cv2.contourArea(contour)
		if area > tooSmall:
			significant.append([contour, area])

			# Draw the contour on the original image
			cv2.drawContours(img, [contour], 0, (0,255,0),2, cv2.LINE_AA, maxLevel=1)

	significant.sort(key=lambda x: x[1])

	f = 0;
	for j in glob.v:
		peri = cv2.arcLength(significant[0][0], True)
		approx = cv2.approxPolyDP(significant[0][0], j * peri, True)
		if len(approx) == 4:
			warped = four_point_transform(orig, approx.reshape(4, 2))
			f = 1
			break

	if f == 0:
		mx = (0,0,0,0)    # biggest bounding box so far
		mx_area = 0
		for cont in contours:
			x,y,w,h = cv2.boundingRect(cont)
			area = w*h
			if area > mx_area:
				mx = x,y,w,h
				mx_area = area
		x,y,w,h = mx
		roi = img[y:y+h,x:x+w]
		lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
		angles = []
		try:
			for [[x1, y1, x2, y2]] in lines:
				angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
				angles.append(angle)
			median_angle = np.median(angles)
			img_rotated = ndimage.rotate(roi, median_angle)
			return img_rotated
		except:
			return None
	else:
		try:
			warped = check_orientation(warped)
		except:
			pass

		text = pytesseract.image_to_string(warped) 
		if information.info(text) > 5:
			return warped
		else:
			mx = (0,0,0,0)
			mx_area = 0
			for cont in contours:
				x,y,w,h = cv2.boundingRect(cont)
				area = w*h
				if area > mx_area:
					mx = x,y,w,h
					mx_area = area
			x,y,w,h = mx
			roi = img[y:y+h,x:x+w]
			lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
			angles = []
			for [[x1, y1, x2, y2]] in lines:
				angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
				angles.append(angle)
			median_angle = np.median(angles)
			img_rotated = ndimage.rotate(roi, median_angle)
			return img_rotated
		return