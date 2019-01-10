from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, TextAreaField,  SubmitField, IntegerField, DateField, SelectField
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
    id = IntegerField('id')
    client = StringField('Client Identifier', validators=[DataRequired()])


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
    product_areas = [
        ('Policies', 'Policies'),
        ('Billing', 'Billing'),
        ('Claims', 'Claims'),
        ('Reports', 'Reports'),
    ]
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    client = SelectField('Client Identity', choices=clients)
    client_priority = IntegerField('Client Priority', validators=[DataRequired()])
    target_date = DateField('Target Date')
    product_area = SelectField('Product Area', choices=product_areas)
    submit = SubmitField('Submit')


class FeatureSearchForm(FlaskForm):
    choices = [('Client', 'Client'),
               ('IWS User', 'IWS User')]

    select = SelectField('Search Features for:', choices=choices)
    search = StringField(' Name')
    submit = SubmitField('Submit')
