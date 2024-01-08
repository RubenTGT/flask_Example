from flask import Blueprint, redirect, render_template, url_for
from services.persons_service import search_person

persons = Blueprint('persons', __name__, template_folder='app/templates')


@persons.route('/')
def index():
    return redirect(url_for('persons.search_person_route'))


@persons.route('/browse_person', methods=['GET','POST'])
def search_person_route():
    return search_person()