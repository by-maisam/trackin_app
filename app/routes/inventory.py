from flask import render_template, redirect, url_for, flash, request, session
from app.routes import inventory_bp
from app.models import db, Asset, License
from datetime import datetime

@inventory_bp.route('/assets')
def list_assets():
    if not session.get('user_id') or session.get('user_role') != 'Admin':
        return redirect(url_for('auth.login'))
    assets = Asset.query.all()
    return render_template('inventory/assets.html', assets=assets)

@inventory_bp.route('/assets/new', methods=['GET', 'POST'])
def new_asset():
    if not session.get('user_id') or session.get('user_role') != 'Admin':
        return redirect(url_for('auth.login'))
        
    if request.method == 'POST':
        serial_number = request.form.get('serial_number')
        model_name = request.form.get('model_name')
        category = request.form.get('category')
        purchase_date_str = request.form.get('purchase_date')
        
        purchase_date = datetime.strptime(purchase_date_str, '%Y-%m-%d').date()
        
        asset = Asset(
            serial_number=serial_number,
            model_name=model_name,
            category=category,
            purchase_date=purchase_date,
            status='Available'
        )
        db.session.add(asset)
        db.session.commit()
        flash('Asset added successfully!', 'success')
        return redirect(url_for('inventory.list_assets'))
        
    return render_template('inventory/assets.html', open_modal=True)

@inventory_bp.route('/licenses')
def list_licenses():
    if not session.get('user_id') or session.get('user_role') != 'Admin':
        return redirect(url_for('auth.login'))
    licenses = License.query.all()
    return render_template('inventory/licenses.html', licenses=licenses)