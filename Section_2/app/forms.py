from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length


# Define the class form the form needed to create an assessment
class AssessmentForm(FlaskForm):
    assessmenttitle = StringField('assessmenttitle',
                                  validators=[DataRequired(), Length(max=300)])
    modulecode = StringField('modulecode',
                             validators=[DataRequired(), Length(max=100)])
    deadline = DateField('deadline',
                         validators=[DataRequired()])
    description = TextAreaField('description',
                                validators=[DataRequired(), Length(max=500)])
    status = BooleanField('status')
