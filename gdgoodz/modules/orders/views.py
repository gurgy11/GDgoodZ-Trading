from flask import Blueprint, request, render_template, redirect, url_for
from gdgoodz.lib.middleware import login_required

bp = Blueprint('orders', __name__)


@bp.route('/orders')
@bp.route('/orders/index')
@login_required
def index():
    return render_template('orders/index.html', title='GDgoodZ Trading - Orders', top_heading_txt='Orders - Index',
                           secondary_heading_txt='View and manage all of your orders below!')


@bp.route('/orders/create', methods=['GET', 'POST'])
@login_required
def create():
    
    if request.method == 'POST':
        supplier = request.form.get('supplier')
        products = request.form.get('products')
        print(products)
    
    return render_template('orders/create.html', title='GDgoodZ Trading - Orders', top_heading_txt='Orders - Create',
                           secondary_heading_txt='Use the form below to create and submit a new order!')