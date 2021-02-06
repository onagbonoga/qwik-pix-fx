import os
from flask import Blueprint, render_template, session
from qpfApp.core.forms import UploadForm
from qpfApp.core.picture_handler import upload_pic, mod_pic
from decimal import Decimal 
core_app = Blueprint('Core', __name__)

@core_app.route('/', methods= ('GET', 'POST'))
def home():

	form = UploadForm()
	if form.validate_on_submit():
		if form.picture.data:
			set_attributes()
			pic = upload_pic(form.picture.data,"test")
			session["current_pic"] = pic
			return render_template("modify.html", pic = pic)
	return render_template("index.html", form = form)

@core_app.route('/edit/<selection>', methods= ('GET', 'POST'))
def edit(selection):

	pic = session["current_pic"]
	mod_pic(selection, pic)
	return f" this is a message from your server {selection}", 200

@core_app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	if 'Cache-Control' not in response.headers:
		response.headers['Cache-Control'] = 'no-store'
	return response 

def set_attributes():
	session["blur_level"] = 0
	session["brightness_level"] = 1.0
	session["sharpness_level"] = 1.0
	session["contrast_level"] = 1.0