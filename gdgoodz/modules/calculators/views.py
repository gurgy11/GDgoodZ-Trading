from flask import Blueprint, request, render_template, redirect, url_for
from gdgoodz.lib.middleware import login_required

bp = Blueprint('calculators', __name__)


@bp.route('/calculators')
@login_required
def calculators():
    return render_template('calculators/index.html', title='GDgoodZ Trading - Calculators', 
                           top_heading_txt='Calculators - Index',
                           secondary_heading_txt='Use the calculators below to test and simulate potential costs!')