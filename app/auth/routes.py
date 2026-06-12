from flask import render_template, redirect, url_for, flash, request, session
from app.auth import auth_bp
from app.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('Email address already registered', 'error')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password, method='scrypt')
        
        new_user = User(
            email=email,
            password_hash=hashed_password,
            full_name=full_name,
            role='Employee'
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Please check your login details and try again.', 'error')
            return redirect(url_for('auth.login'))
        
        session['user_id'] = user.id
        session['user_role'] = user.role
        session['user_name'] = user.full_name
        
        return redirect(url_for('health_check')) # Temporary redirect until dashboards are ready
        
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))