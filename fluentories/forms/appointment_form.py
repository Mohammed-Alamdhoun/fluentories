from wtforms import (StringField, DateField, 
                     SubmitField, EmailField,
                     SelectField, TextAreaField, TimeField)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class AppointmentForm(FlaskForm):
    first_name = StringField('Firest Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=120)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=15)])
    date = DateField('Appointment Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()], format='%H:%M')
    how_heard = SelectField('How Did You Hear About Us', choices=[
        ('', ' Select'),
        ('friend', 'Friend'),
        ('social_media', 'Social Media'),
        ('search_engine', 'Search Engine'),
        ('advertisement', 'Advertisement'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    notes = TextAreaField('Notes', validators=[Length(max=500)])
    submit = SubmitField('Book Appointment')

