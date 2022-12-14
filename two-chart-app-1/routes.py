from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/')
def show():
    try:
        title = "Hey"
        return render_template('main.html', title=title)
    except TemplateNotFound:
        abort(404)
