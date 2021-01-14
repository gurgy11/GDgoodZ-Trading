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
               supplier.street_address, supplier.city, supplier.region, supplier.postal_zip, supplier.country]
        rows.append(row)
    
    table = SupplierTable()
    columns = table.columns
    
    top_heading_txt = 'Suppliers - Index'
    secondary_heading_txt = 'View and manage your complete list of suppliers below!'
    return render_template('suppliers/index.html', title='GDgoodZ Trading - Suppliers', top_heading_txt=top_heading_txt, 
                           secondary_heading_txt=secondary_heading_txt, columns=columns, rows=rows, suppliers=suppliers)


@bp.route('/suppliers/create', methods=['GET', 'POST'])
@login_required
def create():
    ''' Displays the supplier creation form page '''
    
    if request.method == 'POST':
        form = request.form
        errors = controller.create_record(form)
        
        if errors is not None:
            return render_template('suppliers/create.html', title='GDgoodZ Trading - Create Supplier', top_heading_txt='Suppliers - Create', 
                           secondary_heading_txt='Use the form below to create and submit a new supplier!', errors=errors)
        else:
            return redirect(url_for('suppliers.index'))
    
    return render_template('suppliers/create.html', title='GDgoodZ Trading - Create Supplier', top_heading_txt='Suppliers - Create', 
                           secondary_heading_txt='Use the form below to create and submit a new supplier!')


@bp.route('/suppliers/edit/<supplier_id>', methods=['GET', 'POST'])
@login_required
def edit(supplier_id):
    supplier = controller.select_record_by_id(supplier_id)
    
    if request.method == 'POST':
        form = request.form
        
        errors = controller.update_record(supplier_id, form)
        
        if errors is not None:
            return render_template('suppliers/edit.html', title='GDgoodZ Trading - Edit Supplier', top_heading_txt='Suppliers - Edit', 
                           secondary_heading_txt='Use the form below to edit and update a supplier!', supplier=supplier, errors=errors)
        else:
            return redirect(url_for('suppliers.index'))
    
    return render_template('suppliers/edit.html', title='GDgoodZ Trading - Edit Supplier', top_heading_txt='Suppliers - Edit', 
                           secondary_heading_txt='Use the form below to edit and update a supplier!', supplier=supplier)