from flask import render_template, flash, redirect,  url_for, request, g
from app import app
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .forms import FeatureForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Malio'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title='Sign In', form=form,  providers=app.config['OPENID_PROVIDERS'])

@app.route('/feature', methods=['GET', 'POST'])
def feature():
    form = FeatureForm()
    if form.validate_on_submit():
        flash('Title {}, Description={}, Client={}, Client Priority={}, Target Date={}, Product_Area={}'.format(
            form.title.data, form.description.data, form.client.data, form.client_priority.data, form.target_date.data, form.product_area.data))
        return redirect(url_for('feature'))
    return render_template('feature.html', title='Feature Request', form=form)
