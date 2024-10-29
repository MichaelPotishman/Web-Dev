from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    assessmenttitle = StringField('assessmenttitle', validators=[DataRequired()])
    modulecode = StringField('modulecode', validators=[DataRequired()])
    deadline = DateField('deadline', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    status = BooleanField('status')

class NewPropertyForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
