from flask import Blueprint

admin_bp = Blueprint('admin', __name__)
inventory_bp = Blueprint('inventory', __name__)

from app.routes import admin, inventory