from datetime import datetime

from flask_wtf import FlaskForm
from flask import current_app
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    dob = DateField('Date of birth', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    submit = SubmitField("Submit")

    def validate_dob(self, dob):
        if dob.data > datetime.today().date():
                raise ValidationError("Invalid date")
