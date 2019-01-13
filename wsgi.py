
import sys

# add your project directory to the sys.path
project_home = u'/home/dmueni/feature-request-app'
if project_home not in sys.path:
     sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from features import app as application
if __name__ == "__main__":
    app.run()
