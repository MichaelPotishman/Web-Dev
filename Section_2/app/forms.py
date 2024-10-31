from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length

class AssessmentForm(FlaskForm):
    assessmenttitle = StringField('assessmenttitle', validators=[DataRequired(), Length(max=300)])
    modulecode = StringField('modulecode', validators=[DataRequired(), Length(max=100)])
    deadline = DateField('deadline', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired(), Length(max=500)])
    status = BooleanField('status')

class NewPropertyForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
