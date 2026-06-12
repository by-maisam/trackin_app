from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

license_assignments = db.Table('license_assignments',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('license_id', db.Integer, db.ForeignKey('licenses.id', ondelete='CASCADE'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    db.Column('assigned_at', db.DateTime, default=datetime.utcnow)
)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='Employee', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    assets = db.relationship('Asset', backref='assigned_user', lazy=True)
    licenses = db.relationship('License', secondary=license_assignments, 
                               backref=db.backref('assigned_users', lazy='dynamic'))

class Asset(db.Model):
    __tablename__ = 'assets'
    
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(30), default='Available', nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)

class License(db.Model):
    __tablename__ = 'licenses'
    
    id = db.Column(db.Integer, primary_key=True)
    software_name = db.Column(db.String(100), nullable=False)
    license_key = db.Column(db.String(255), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Numeric(10, 2), default=0.00, nullable=False)