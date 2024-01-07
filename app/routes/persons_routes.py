from flask import Blueprint, render_template
from services.persons_service import search_person

persons = Blueprint('contacts', __name__, template_folder='app/templates')


@persons.route('/')
def Index():
    return render_template('index.html')


@persons.route('/browse_person', methods=['POST'])
def search_person_route():
    return search_person()