from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, BooleanField
from flask_wtf.html5 import URLField
from wtforms.validators import InputRequired, url, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species=SelectField("Species", choices=[('cat', 'cat'),('dog', 'dog'),('pcp', 'porcupine')], validators=[InputRequired()])
    photo_url=URLField("Photo URL", validators=[Optional()])
    age=IntegerField("Age (years)", validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30"), Optional()])
    notes=StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets. Editing allows for change in photo, notes, and availability"""
    photo_url=URLField("Photo URL", validators=[Optional()])
    notes=StringField("Notes", validators=[Optional()])
    available=BooleanField(default="checked")