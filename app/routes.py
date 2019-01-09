from flask import render_template, flash, redirect, session, url_for, request, g
from app import app,db
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, ClientForm, FeatureForm, FeatureSearchForm
from .models import User, Feature, Client
from .tables import Results
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from .database import db_session


@app.route('/', methods=['GET', 'POST'])
@app.route('/')

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    search = FeatureSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', title='Home', form=search)

@app.route('/results')
def search_results(*args):
    search = FeatureSearchForm(request.form)
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Feature)
        results = Feature.query.all()
       
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = False
        return render_template('results.html', table=table)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/feature', methods=['GET', 'POST'])
@login_required
def feature():
    form = FeatureForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the New Feature
        feature = Feature()
        save_changes(feature, form, new=True)
        flash('Feature Request Submitted successfully!')
        return redirect(url_for('feature'))
  
    return render_template('feature.html', title='Feature Request', form=form)

def save_changes(feature, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    new_client = Client()
    new_client.name = form.client.data
 
    feature.title = form.title.data
    feature.description = form.description.data
    feature.client = form.client.data
    feature.client_priority = form.client_priority.data
    feature.target_date = form.target_date.data
    feature.product_area = form.product_area.data
    
    if new:
        # Add the new feature to the database
        db_session.add(feature)
 
    # commit the data to the database
    db_session.commit()

if __name__ == "__main__":
    app.run()