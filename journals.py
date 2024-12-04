from flask import Blueprint, render_template, request, jsonify, redirect
from models import Journal, db
from datetime import date, time, datetime
from sqlalchemy import desc



journal_bp = Blueprint('journal', __name__)

@journal_bp.route('/', methods=['GET', 'POST'])
def journals():
    # Add journal if the call to /journal is a POST call
    if request.method == 'POST':
        # form passes date as string, we need to convert to python date object as below
        journal_date=datetime.strptime(request.values['journalDate'], '%Y-%m-%d').date()
        time_hr = int(request.values['journalTime'][:2])
        time_min = int(request.values['journalTime'][3:])
        new_journal = Journal( date = journal_date, text= request.values['journalText'], time =time(time_hr,time_min))
        try:
            db.session.add(new_journal)
            db.session.commit()
        except Exception as e:
            return 'error while adding journal', 500
    # Get the Journals data to display on the frontend
    journals=Journal.query.order_by(desc(Journal.date),Journal.time).distinct().all()
    # we need to format date in journal to string so it can be used in jinja2 template to group by day
    for journal in journals:
        journal.date_str = journal.date.strftime('%Y-%m-%d')
    #pass the journals data and render the journals html for GET as well as POST
    return render_template('journals.html', journals=journals),200
    

