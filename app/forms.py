from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ClientForm(FlaskForm):
    client = StringField('Title', validators=[DataRequired()])
   

class FeatureForm(FlaskForm):
    clients = [
        ('Client A', 'Client A'),
        ('Client B', 'Client B'),
        ('Client C', ' Client C'), 
        ('Client E', ' Client E'), 
        ('Client D', ' Client D'), 
        ('Client F', ' Client F'), 
        ('Client H', ' Client H')
                ]
    priorities = [
        ('1', '1'), 
        ('2', '2'),
        ('3', '3'), 
        ('4', '4'),
        ('5', '5'), 
        ('6', '6')
    ]
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    client = SelectField('Client Identity', choices=clients )
    client_priority = SelectField('Client Priority', choices=priorities)
    target_date = DateField('Target Date')
    product_area = StringField('Product Area', validators=[DataRequired()])
    submit = SubmitField('Submit')

