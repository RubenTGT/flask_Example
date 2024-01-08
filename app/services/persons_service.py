from flask import jsonify, render_template, request
from database.db_connection import mysql
from datetime import datetime

def search_person():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM personal_info WHERE first_name = %s AND last_name = %s', (name, last_name))
        result = cur.fetchall()

        response = {"encontrado": len(result) > 0}

        log_query(datetime.now(), f"Name: {name}, Last Name: {last_name}", str(response))

        return jsonify(response)
    else:
        return render_template('index.html')

def log_query(query_date, request_parameters, result):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO query_log (query_date, request_parameters, result) VALUES (%s, %s, %s)',
                (query_date, request_parameters, result))
    mysql.connection.commit()
    cur.close()