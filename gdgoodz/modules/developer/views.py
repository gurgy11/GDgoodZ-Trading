from flask import Blueprint, request, render_template, redirect, url_for, send_file, jsonify
from gdgoodz.lib.middleware import login_required
from .controller import DeveloperController

bp = Blueprint('developer', __name__)
controller = DeveloperController()


@bp.route('/developer')
@bp.route('/developer/index')
@login_required
def index():
    return render_template('developer/index.html', title='GDgoodZ Trading - Developer', 
                           top_heading_txt='Developer - Index',
                           secondary_heading_txt="This page is meant as a test page for components!")
    

@bp.route('/developer/fetchall/products')
@login_required
def fetchall_products():
    products = controller.fetchall_products_as_dicts()
    return jsonify(products)