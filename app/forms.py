from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png', 'Images Only!'])
    ])