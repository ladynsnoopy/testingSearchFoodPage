from wtforms import Form,StringField,validators
from wtforms.validators import InputRequired


class RegistrationForm(Form):
    foodname = StringField('Search Food',validators=[InputRequired()])
