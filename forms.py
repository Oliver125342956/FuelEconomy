from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Forms(FlaskForm):
    origin = StringField('Original Location', validators=[DataRequired(), Length(min=1, max=25)])
    destination = StringField('Destination', validators=[DataRequired(), Length(min=1, max=25)])
    calculate = SubmitField('Calculate')
    