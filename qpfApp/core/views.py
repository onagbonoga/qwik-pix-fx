from flask import Blueprint, render_template
from qpfApp.core.forms import UploadForm
from qpfApp.core.picture_handler import upload_pic
core_app = Blueprint('Core', __name__)

@core_app.route('/', methods= ('GET', 'POST'))
def home():
	form = UploadForm()
	if form.validate_on_submit():
		if form.picture.data:
			pic = upload_pic(form.picture.data,"test")
			return render_template("modify.html", pic = pic)
	return render_template("index.html", form = form)

@core_app.route('/edit photo')
def edit():
	return "Hi"