from features import app, db
from features.models import User, Feature,Client

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Feature': Feature, 'Client':Client}

if __name__ == "__main__":
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)
