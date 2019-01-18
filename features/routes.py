from flask import render_template, flash, redirect, session, url_for, request, jsonify
from features import app, db
from flask_login import login_user, logout_user, current_user, login_required
from features.forms import LoginForm, ClientForm, FeatureForm, FeatureSearchForm, RegistrationForm
from features.models import User, Feature, Client
from features.tables import Results
from werkzeug.urls import url_parse
from .database import db_session


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    search = FeatureSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', title='Home', form=search)


@app.route('/results', methods=['GET', 'POST'])
@login_required
def search_results(*args):
    search = FeatureSearchForm(request.form)
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Feature)
        
        results = Feature.query.order_by(Feature.client_priority).all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Feature).filter(
        Feature.id == id)
    feature = qry.first()

    if feature:
        form = FeatureForm(formdata=request.form, obj=feature)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(feature, form)
            flash('Feature updated successfully!')
            return redirect('/')
        return render_template('edit_feature.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


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
            next_page = url_for('feature')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET', 'POST'])
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
        feature.title = form.title.data
        feature.description = form.description.data
        feature.client = form.client.data
        feature.client_priority = form.client_priority.data
        feature.target_date = form.target_date.data
        feature.product_area = form.product_area.data

        priority=form.client_priority.data
        #right here I call the save_duplicates function
        save_duplicates(feature, form, priority, True)
        flash('Feature Request Submitted successfully!')
        return redirect(url_for('feature'))
    return render_template('feature.html', title='Feature Request', form=form)

def save_duplicates(feature,form, priority, first=False):
    print("we are coding", priority)
    feature_detail=Feature.query.filter(Feature.client==feature.client).filter(Feature.client_priority==priority).first()
    # feature_detail.compile().params
    print("=========",feature_detail)
    if feature_detail:
        save_duplicates(feature_detail, None, priority+1)
        # feature = feature_detail
        priority = None
        save_changes(feature, form, priority)
    else:
        if first:
            save_changes(feature, form, None)
        else:
            save_changes(feature, form, priority)

def save_changes(feature_detail, form, priority=None):
    if form:
        #saving the data into the database
        feature_detail.title = form.title.data
        feature_detail.description = form.description.data
        feature_detail.client = form.client.data
        feature_detail.client_priority = form.client_priority.data
        feature_detail.target_date = form.target_date.data
        feature_detail.product_area = form.product_area.data
    if priority:
        new_feature = Feature.query.filter(Feature.client==feature_detail.client).first()
        feature_2 = Feature()
        feature_2.title = new_feature.title
        feature_2.description = new_feature.description
        feature_2.client = new_feature.client
        feature_2.client_priority = priority
        feature_2.target_date = new_feature.target_date
        feature_2.product_area = new_feature.product_area
        db.session.remove()
        db_session.delete(new_feature)
    
        db_session.add(feature_2)
        db_session.commit()
        db.session.remove()
        
    else:
        db_session.add(feature_detail)
        db_session.commit()
        db.session.remove()
     



