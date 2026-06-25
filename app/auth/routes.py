from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        u_email = request.form.get('email')
        u_role = request.form.get('role')
        pass_word = request.form.get('password')
        
        existing_user = User.query.filter_by(email=u_email).first()
        if existing_user:
            flash('That email is already taken.', 'error')
            return redirect(url_for('auth.register'))
            
        new_user = User(name=full_name, email=u_email, role=u_role)
        new_user.hash_password(pass_word)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created! You can log in now.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_input = request.form.get('email')
        pass_input = request.form.get('password')
        
        user = User.query.filter_by(email=email_input).first()
        
        if user and user.verify_password(pass_input):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_role'] = user.role
            return redirect(url_for('admin.dashboard'))
            
        flash('Wrong email or password.', 'error')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))