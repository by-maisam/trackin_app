from flask import render_template, redirect, url_for, flash, request, session
from app.routes import admin_bp
from app.models import db, Asset, License, User

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
        
    if session.get('user_role') == 'Employee':
        user_assets = Asset.query.filter_by(assigned_to_id=session.get('user_id')).all()
        return render_template('admin/ui/dashboard.html', assets=user_assets, is_admin=False)
        
    total_assets = Asset.query.count()
    assigned_assets = Asset.query.filter_by(status='Assigned').count()
    available_assets = Asset.query.filter_by(status='Available').count()
    
    licenses = License.query.all()
    total_spend = sum(float(l.cost) for l in licenses)
    
    users = User.query.filter_by(role='Employee').all()
    
    return render_template(
        'admin/ui/dashboard.html',
        is_admin=True,
        total_assets=total_assets,
        assigned_assets=assigned_assets,
        available_assets=available_assets,
        total_spend=total_spend,
        licenses=licenses,
        users=users
    )

@admin_bp.route('/assign/asset/<int:id>', methods=['POST'])
def assign_asset(id):
    if not session.get('user_id') or session.get('user_role') != 'Admin':
        return redirect(url_for('auth.login'))
        
    asset = Asset.query.get_or_404(id)
    user_id = request.form.get('user_id')
    
    if not user_id:
        asset.assigned_to_id = None
        asset.status = 'Available'
    else:
        asset.assigned_to_id = user_id
        asset.status = 'Assigned'
        
    db.session.commit()
    flash(f'Asset {asset.serial_number} assignment updated successfully.', 'success')
    return redirect(url_for('admin.dashboard'))