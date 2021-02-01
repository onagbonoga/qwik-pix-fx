from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
	picture = FileField('Upload File', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Upload')

	def validate(self):
		if not FlaskForm.validate(self):
			return False

		return True
