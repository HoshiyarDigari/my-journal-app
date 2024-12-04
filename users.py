from flask import Blueprint, render_template, request, redirect
from models import User

user_bp=Blueprint('user',__name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # if the request is for login
        if request.values.get('login'):
            return redirect('/journal')
        elif request.values.get('sign-up'):
            return "you are registered"
    