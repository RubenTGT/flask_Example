from flask import Blueprint, render_template

persons = Blueprint('contacts', __name__, template_folder='app/templates')


@persons.route('/')
def Index():
    return render_template('index.html')