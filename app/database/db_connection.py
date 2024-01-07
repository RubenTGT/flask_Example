from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = 'flask_project'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flask_project'

mysql = MySQL(app)
