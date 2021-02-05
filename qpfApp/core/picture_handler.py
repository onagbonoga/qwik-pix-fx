import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from flask import url_for, current_app, session

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

	session["blur_level"] = 0

	if command == "blur plus":
		session["blur_level"] = session["blur_level"] + 1
		pic = pic.filter(ImageFilter.GaussianBlur(session["blur_level"]))

	if command == "blur minus":
		session["blur_level"] = session["blur_level"] - 1
		pic = original_pic.filter(ImageFilter.GaussianBlur(session["blur_level"]))

	#pic.show()
	pic.save(filepath)

