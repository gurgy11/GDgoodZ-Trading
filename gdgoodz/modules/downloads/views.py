from flask import Blueprint, request, redirect, url_for, send_file

bp = Blueprint('downloads', __name__)


@bp.route('/downloads/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)