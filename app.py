# journal app basic entry file
from flask import Flask, render_template, request, jsonify, redirect
from models import Journal, db
from datetime import date, time, datetime
from sqlalchemy import desc
from journals import journal_bp
from users import user_bp

app = Flask(__name__)

# database initialize and config
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///journal.db'
db.init_app(app)


#register blueprints for routes
app.register_blueprint(journal_bp, url_prefix='/journal')
app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/', methods=['GET'])
def login():
    return redirect('/user/login')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5004)
