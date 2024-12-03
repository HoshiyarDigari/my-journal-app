from flask import Blueprint, render_template, request, jsonify, redirect
from models import Journal, db
from datetime import date, time, datetime
from sqlalchemy import desc


user_bp = Blueprint('user', __name__)

@user_bp.route('/journals', methods=['GET', 'POST'])
def journals():
    if request.method == 'GET':
        return render_template('journals.html')
    elif request.method == 'POST':
        # form passes date as string, we need to convert to python date object as below
        journal_date=datetime.strptime(request.values['journalDate'], '%Y-%m-%d').date()
        print('journal date in request', request.values['journalDate'], journal_date)
        time_hr = int(request.values['journalTime'][:2])
        time_min = int(request.values['journalTime'][3:])
        # print(time_hr, time_min)
        new_journal = Journal( date = journal_date, text= request.values['journalText'], time =time(time_hr,time_min))
        try:
            db.session.add(new_journal)
            db.session.commit()
        except Exception as e:
            return 'error while adding journal', 500
        # query db for all of existing journals and return them sorted with last entry first
        journals=Journal.query.order_by(desc(Journal.date),Journal.time).all()
        # we need to format date in journal to string so it can be used in jinja2 template to group by day
        for journal in journals:
            journal.date_str = journal.date.strftime('%Y-%m-%d')
        return render_template('journals.html', journals=journals)
            