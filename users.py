from flask import Blueprint, render_template
from models import User

user_bp=Blueprint('user',__name__)

@user_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')