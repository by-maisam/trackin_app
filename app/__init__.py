from flask import Flask
from config import Config
from app.models import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    
    from app.routes import admin_bp, inventory_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(inventory_bp)
    
    return app