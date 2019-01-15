from flask import render_template, flash, redirect, session, url_for, request, jsonify
from features import app, db
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, ClientForm, FeatureForm, FeatureSearchForm, RegistrationForm
from .models import User, Feature, Client
from .tables import Results
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
        results = Feature.query.order_by(Feature.client).all()

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
        save_changes(feature, form, new=True)

        flash('Feature Request Submitted successfully!')

        return redirect(url_for('feature'))

    return render_template('feature.html', title='Feature Request', form=form)



def sort(i_list):
    for val in range(len(i_list)-1, -1, -1):
        swapped = False
        for i in range(val):
            if i_list[i]['client_priority'] >= i_list[i+1]['client_priority']:
                i_list[i], i_list[i+1] = i_list[i+1], i_list[i]
                if i_list[i]['client_priority'] == i_list[i+1]['client_priority']:
                    if i_list[i+1]['date_created']<i_list[i]['date_created']:
                        i_list[i+1]['client_priority'] = i_list[i+1]['client_priority']+1
                swapped = True
        if not swapped:
            break

def save_changes(feature, form, new=False):
    """
    Save the changes to the database
    """
    client_list = []
    client = Feature.query.filter_by(client=form.client.data).filter(Feature.client_priority>=form.client_priority.data)
    for c in client:
        obj = {
            'id': c.id,
            'title': c.title,
            'description': c.description,
            'client': c.client,
            'client_priority': c.client_priority,
            'target_date': c.target_date,
            'product_area': c.product_area, 
            'date_created': c.date_created
        }
        client_list.append(obj)
    sort(client_list)
    print("sharon", client_list)
    for c in client_list:
        feature.client_priority += 1
        db.session.add(feature)
        db.session.commit()

    # Get data from form and assign it to the correct attributes
    client = form.client.data
    print(client)

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
    app.run(host='0.0.0.0')
