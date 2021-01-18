from flask import Blueprint, request, redirect, url_for, send_file
from gdgoodz.lib.middleware.authenticator import login_required

bp = Blueprint('downloads', __name__)


@bp.route('/downloads/<path:filename>')
@login_required
def download(filename):
    return send_file(filename, as_attachment=True)