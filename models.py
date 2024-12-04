from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# database for a Journal 
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)

#user information database
class User(db.Model):
    email =db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(40), nullable=False)
    
