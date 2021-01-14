from flask import Blueprint, request, render_template, redirect, url_for, send_file
from gdgoodz.lib.middleware import login_required
from . import SupplierController, SupplierTable

bp = Blueprint('suppliers', __name__)
controller = SupplierController()


@bp.route('/suppliers')
@bp.route('/suppliers/index')
@login_required
def index():
    ''' Displays all suppliers in the database '''
    
    suppliers = controller.select_all_records()
    rows = []
    
    for supplier in suppliers:
        row = [supplier.id, supplier.name, supplier.email_address, supplier.phone_number, supplier.website_url, 
               supplier.street_address, supplier.city, supplier.region, supplier.postal_zip, supplier.country, 
               supplier.created_at, supplier.updated_at]
        rows.append(row)
    
    table = SupplierTable()
    columns = table.columns
    
    top_heading_txt = 'Suppliers - Index'
    secondary_heading_txt = 'View and manage your complete list of suppliers below!'
    return render_template('suppliers/index.html', title='GDgoodZ Trading - Suppliers', top_heading_txt=top_heading_txt, 
                           secondary_heading_txt=secondary_heading_txt, columns=columns, rows=rows, suppliers=suppliers)