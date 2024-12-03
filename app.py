# journal app basic entry file
from flask import Flask, render_template, request, jsonify
from models import Journal, db
from datetime import date, time, datetime
from sqlalchemy import desc
from userFunctions import user_bp

app = Flask(__name__)

# database initialize and config
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///journal.db'
db.init_app(app)


#register blueprints for routes
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=False, port=5004)
