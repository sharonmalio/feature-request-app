from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class FeatureForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    client = StringField('Client Identifier', validators=[DataRequired()])
    client_priority = StringField('Client Priority', validators=[DataRequired()])
    target_date = DateField('Target Date')
    product_area = StringField('Product Area', validators=[DataRequired()])
    submit = SubmitField('Sign In')