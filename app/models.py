from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='Employee')

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Asset(db.Model):
    __tablename__ = 'assets'
    
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='Available')
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', backref='assigned_assets')


class License(db.Model):
    __tablename__ = 'licenses'
    
    id = db.Column(db.Integer, primary_key=True)
    software_name = db.Column(db.String(100), nullable=False)
    license_key = db.Column(db.String(100), unique=True, nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Float, nullable=False)