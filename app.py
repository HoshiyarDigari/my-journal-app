# journal app basic entry file
from flask import Flask
from models import  db
from journals import journals_bp

app = Flask(__name__)

# database initialize and config
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///journal.db'
db.init_app(app)


#register blueprints for routes
app.register_blueprint(journals_bp, url_prefix='/journal')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5004)
