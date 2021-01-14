from flask import Blueprint, request, render_template, redirect, url_for, send_file
from . import ProductController
from .table import ProductTable
from gdgoodz.lib.middleware import login_required

bp = Blueprint('products', __name__)
controller = ProductController()


@bp.route('/products/inventory')
@login_required
def inventory():
    ''' Full inventory of products '''
    
    products = controller.select_all_products()
    rows_dict = []
    
    for p in products:
        desc = p.description[:40] + '...'
        row = [p.id, p.name, p.category, desc, p.sku, p.status, p.supplier, p.country_of_origin, p.quantity, p.quantity_sold, 
                  p.cost_per_unit, p.price_per_unit, p.notes]
        rows_dict.append(row)
    
    product_table = ProductTable()
    table_columns = product_table.columns
    
    top_heading_txt = 'Products - Inventory'
    secondary_heading_txt = 'View and manage your complete list of products below!'
    return render_template('products/inventory.html', title='GDgoodZ Trading - Products', top_heading_txt=top_heading_txt, 
                           secondary_heading_txt=secondary_heading_txt, columns=table_columns, rows=rows_dict, products=products)
    
    
@bp.route('/products/new')
@login_required
def new():
    ''' Inventory of newly added products '''
    
    top_heading_txt = 'Products - New'
    secondary_heading_txt = 'View and manage your newest products below!'
    return render_template('products/new.html', title='GDgoodZ Trading - New Products', top_heading_txt=top_heading_txt, 
                           secondary_heading_txt=secondary_heading_txt)
    

@bp.route('/products/out_of_stock')
@login_required
def out_of_stock():
    ''' Displays products that are currently out of stock '''
    
    top_heading_txt = 'Products - Out of Stock'
    secondary_heading_txt = 'View and manage your out of stock products below!'
    return render_template('products/out_of_stock.html', title='GDgoodZ Trading - Out of Stock Products', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt)


@bp.route('/products/unlisted')
@login_required
def unlisted():
    ''' Displays the products in stock but not listed for sale '''
    
    top_heading_txt = 'Products - Unlisted'
    secondary_heading_txt = 'View and manage your unlisted products below!'
    return render_template('products/unlisted.html', title='GDgoodZ Trading - Unlisted Products', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt)


@bp.route('/products/incoming')
@login_required
def incoming():
    ''' Shows products that are incoming from an order but not yet arrived or ready for sale '''
    
    top_heading_txt = 'Products - Incoming'
    secondary_heading_txt = 'View and manage your incoming products below!'
    return render_template('products/incoming.html', title='GDgoodZ Trading - Incoming Products', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt)
    

@bp.route('/products/export/xlsx')
@login_required
def export_xlsx():
    ''' Starts a download of the product inventory in an XLSX file '''
    
    product_models = controller.select_all_products()
    product_dicts = controller.product_models_to_dict(product_models)
    
    products_df = controller.product_dicts_to_dataframe(product_dicts)
    file_path = controller.products_dataframe_to_excel(products_df)
    
    return send_file(file_path, as_attachment=True)

@bp.route('/products/export/csv')
@login_required
def export_csv():
    ''' Exports the inventory of products in a CSV file '''
    
    pass


@bp.route('/products/export/json')
@login_required
def export_json():
    ''' Exports the inventory of products as a JSON file '''
    
    pass


@bp.route('/products/create', methods=['GET', 'POST'])
@login_required
def create():
    ''' Displays the create product form page '''
    
    top_heading_txt = 'Products - Create New'
    secondary_heading_txt = 'Use the form below to create and submit a new product!'
    
    if request.method == 'POST':
        product_form = request.form
        errors = controller.create_new_product(product_form)
        
        if errors is not None:
            return render_template('products/create.html', title='GDgoodZ Trading - Create New Product', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt, errors=errors)
        else:
            return redirect(url_for('products.inventory'))
    
    return render_template('products/create.html', title='GDgoodZ Trading - Create New Product', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt)
    

@bp.route('/products/edit/<product_id>', methods=['GET', 'POST'])
@login_required
def edit(product_id):
    ''' Displays the product edit form and submits to the database '''
    
    top_heading_txt = 'Products - Edit'
    secondary_heading_txt = 'Use the form below to edit the product\'s fields!'
    
    # Fetch the original product in case of errors and needing to reload the page
    product = controller.select_product_by_id(product_id)
    
    # Process the POST request when the form is submitted
    if request.method == 'POST':
        product_form = request.form
        
        # Update the product but if their are errors, an array is returned, else, None is returned
        errors = controller.edit_product(product_id, product_form)
        
        # Check for errors
        if errors is not None: # There are errors
            return render_template('products/edit.html', title='GDgoodZ Trading - Edit a Product', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt, product=product, errors=errors)
        else:
            return redirect(url_for('products.inventory'))
    
    return render_template('products/edit.html', title='GDgoodZ Trading - Edit a Product', 
                           top_heading_txt=top_heading_txt, secondary_heading_txt=secondary_heading_txt, product=product)


@bp.route('/products/delete/<product_id>')
@login_required
def delete(product_id):
    controller.delete_product(product_id)
    
    return redirect(url_for('products.inventory'))