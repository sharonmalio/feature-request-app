# import flask app but need to call it "application" for WSGI to work
from features import app


if __name__ == "__main__":
    app.run()
