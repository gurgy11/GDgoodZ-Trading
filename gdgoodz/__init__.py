import os

from flask import Flask, render_template
from dotenv import load_dotenv

from gdgoodz.lib.middleware import login_required

# Load environment variables
load_dotenv()

def create_app(test_config=None):
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY')
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    @app.route('/index')
    @login_required
    def index():
        return render_template('index.html', title='GDgoodZ Trading - Index')
    
    ''' Blueprint Imports '''
    
    from gdgoodz.modules.auth import auth_bp
    app.register_blueprint(auth_bp)
    app.add_url_rule('/', endpoint='auth')
    
    from gdgoodz.modules.products import product_bp
    app.register_blueprint(product_bp)
    app.add_url_rule('/', endpoint='products')
    
    from gdgoodz.modules.suppliers import supplier_bp
    app.register_blueprint(supplier_bp)
    app.add_url_rule('/', endpoint='suppliers')
    
    from gdgoodz.modules.calculators import calculators_bp
    app.register_blueprint(calculators_bp)
    app.add_url_rule('/', endpoint='calculators')
    
    from gdgoodz.modules.orders import orders_bp
    app.register_blueprint(orders_bp)
    app.add_url_rule('/', endpoint='orders')
    
    return app