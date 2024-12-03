from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# template for a journal entry
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)


