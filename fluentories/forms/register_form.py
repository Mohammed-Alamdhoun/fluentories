from wtforms import StringField, DateField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=120)])
    age = IntegerField('Age', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=15)])

    academic_level = SelectField('Academic Level', choices=[
    ('', 'Select'),
    ('high_school', 'High School'),
    ('undergraduate', 'Undergraduate'),
    ('graduate', 'Graduate'),
    ('postgraduate', 'Postgraduate'),
    ('other', 'Other')
    ], validators=[DataRequired()])

    how_heard = SelectField('How Did You Hear About Us', choices=[
    ('', 'Select'),
    ('friend', 'Friend'),
    ('social_media', 'Social Media'),
    ('search_engine', 'Search Engine'),
    ('advertisement', 'Advertisement'),
    ('other', 'Other')
    ], validators=[DataRequired()])
    availability_time = DateField('Availability Date', validators=[DataRequired()])
    submit = SubmitField('Register')