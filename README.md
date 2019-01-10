git clone......
 pip install -r requirements.txt
flask run -p 5000

Installing the dependencies
The first thing we need to do is install some third party libraries for Python. These are:

Flask, which we'll use to route web traffic through HTTP requests to specific functions in our code base,
SQLAlchemy, which we'll use to make the interaction between Python and our database smoother,
Flask-SQLAlchemy, which we'll use to make the interaction between Flask and SQLAlchemy smoother.
You can install all of these through pip by running the following command:

pip3 install --user flask sqlalchemy flask-sqlalchemy