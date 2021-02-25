import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
from flask import url_for, current_app, session
from qpfApp import app 
import numpy as np


#getcontext().prec = 1


def upload_pic(pic_upload, name):
	filename = pic_upload.filename
	ext_type = filename.split('.')[-1] #get the extension type of the file
	storage_filename = str(name) + '.' + ext_type
	storage_filename_copy = 'copy' + str(name) + '.' + ext_type

	filepath = os.path.join(current_app.root_path,'static/pictures', storage_filename) #renames picture
	filepath_copy = os.path.join(current_app.root_path,'static/pictures', storage_filename_copy)
	#making sure everything is the same size
	#output_size = (1000,1000)
	pic = Image.open(pic_upload)
	#pic.thumbnail(output_size)
	pic.save(filepath)

	#saves a copy of the original image that will not be changed
	pic.save(filepath_copy)
	return storage_filename

def mod_pic(command, pic):
	filepath = os.path.join(current_app.root_path,'static/pictures', pic)
	filepath_copy = os.path.join(current_app.root_path,'static/pictures', "copy" + pic)
	pic = Image.open(filepath)
	original_pic = Image.open(filepath_copy)
	brightness_level = 0
	if command == "blur plus":
		session["blur_level"] = session["blur_level"] + 1
		#pic = original_pic.filter(ImageFilter.GaussianBlur(session["blur_level"]))

	if command == "blur minus":
		session["blur_level"] = session["blur_level"] - 1
		#pic = original_pic.filter(ImageFilter.GaussianBlur(session["blur_level"]))

	if command == "sharpen":
		pic = pic.filter(ImageFilter.SHARPEN)

	if command == "edge enhance":
		pic = pic.filter(ImageFilter.EDGE_ENHANCE)

	if command == "refresh":
		set_attributes()
		pic = original_pic

	if command == "brightness plus":
		session["brightness_level"] = round(float(Decimal(session["brightness_level"]) + Decimal(0.1)),1)
		'''pic = original_pic
		enhancer = ImageEnhance.Brightness(pic)
		pic = enhancer.enhance(session["brightness_level"])'''

	if command == "brightness minus":
		session["brightness_level"] = round(float(Decimal(session["brightness_level"]) - Decimal(0.1)),1)
		#brightness_level = str(session["brightness_level"])
		#brightness_level = float(brightness_level)
		'''pic = original_pic
		enhancer = ImageEnhance.Brightness(pic)
		pic = enhancer.enhance(session["brightness_level"])'''

	if command == "contrast plus":
		session["contrast_level"] = round(float(Decimal(session["contrast_level"]) + Decimal(0.2)),1)

	if command == "contrast minus":
		session["contrast_level"] = round(float(Decimal(session["contrast_level"]) - Decimal(0.2)),1)

	if command == "sharpness plus":
		session["sharpness_level"] = round(float(Decimal(session["sharpness_level"]) + Decimal(0.1)),1)

	if command == "sharpness minus":
		session["sharpness_level"] = round(float(Decimal(session["sharpness_level"]) - Decimal(0.1)),1)

	if command == "saturation plus":
		session["saturation_level"] = round(float(Decimal(session["saturation_level"]) + Decimal(0.2)),1)

	if command == "sharpness minus":
		session["saturation_level"] = round(float(Decimal(session["saturation_level"]) - Decimal(0.2)),1)

	if command == "vertical flip":
		session["vertical_flip"] ^= 1

	if command == "horizontal flip":
		session["horizontal_flip"] ^= 1

	if command == "grayscale":
		session["grayscale"] ^= 1

	if command == "invert":
		session["invert"] ^= 1

	if command == "filter1":
		if session["filter"] == 1:
			session["filter"] = 0
		else:
			session["filter"] = 1



	#apply modifications
	pic = original_pic.filter(ImageFilter.GaussianBlur(session["blur_level"]))
	enhancer = ImageEnhance.Brightness(pic)
	pic = enhancer.enhance(session["brightness_level"])
	enhancer = ImageEnhance.Sharpness(pic)
	pic = enhancer.enhance(session["sharpness_level"])
	enhancer = ImageEnhance.Contrast(pic)
	pic = enhancer.enhance(session["contrast_level"])
	enhancer = ImageEnhance.Color(pic)
	pic = enhancer.enhance(session["saturation_level"])
	pic = applyFilter(session["filter"],pic)

	#i'm putting these effects at this point in the file so adding one of the effects below wont overwrite any of the effects above

	if session["vertical_flip"] == 1:
		pic = ImageOps.flip(pic)

	if session["horizontal_flip"] == 1:
		pic = ImageOps.mirror(pic)

	if session["grayscale"] == 1:
		pic = ImageOps.grayscale(pic)

	if session["invert"] == 1:
		pic = ImageOps.invert(pic)
	#print(session["brightness_level"])
	#pic.show()
	pic.save(filepath)

def set_attributes():
	session["blur_level"] = 0
	session["brightness_level"] = 1.0
	session["sharpness_level"] = 1.0
	session["contrast_level"] = 1.0
	session["saturation_level"] = 1.0
	session["vertical_flip"] = 0
	session["horizontal_flip"] = 0
	session["grayscale"] = 0
	session["invert"] = 0
	session["filter"] = 0 #no filter


def applyFilter(filter,image):
	if filter == 1:
		pic_array = np.asarray(image) #converts the image to a numpy array
		pic = pic_array.copy()
		pic[:,:,2] = pic[:,:,2] + 10

		for pixel in np.nditer(pic,op_flags = ['readwrite']): #iterates through the array
			if pixel > 180:
				pixel[...] = pixel - 20
		finalPic = Image.fromarray(pic)
		return finalPic
	if filter == 0:
		return image

'''this function modifies the image values directly with numpy
	image -> image input
	channel -> channel to modify. valid inputs: 0,1,2 (reg green or blue)
	section -> section to modify. Valid inputs:	B,S,M,H,W (Black, Shadows, Midtones, Highlights, White)
	delta -> how much to change the section of the image to 
'''
'''def rgbMod(image,channel,section,delta):
	if section == B:
		val = 0
	elif section == S:
		val = 63
	elif section == M:
		val = 127
	elif section == H:
		val = 191
	elif section == W:
		val = 255

	pic_array = np.asarray(image) #converts the image to a numpy array
	pic = pic_array.copy()
	size1 = pic.shape[0]
	size2 = pic.shape[1]

	for pixel in np.nditer(pic,op_flags = ['readwrite']): #iterates through the array
		if pixel == val:
			pixel[...] = pixel + delta
		if ((pixel > val and pixel < val + 16) or (pixel > val and pixel < val  16)) and delta - 1 > 0 and delta > 0:
			pixel[...] pixel + delta 

	pic[:,:,channel] = pic[:,:,channel] + modArray(delta,size1,size2)


this function generates a numpy array that will be added to an image
	to modify the color values

def modArray(value,size1,size2): 
	for pixel in np.nditer()'''

