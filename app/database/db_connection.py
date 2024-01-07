from app import app
from decouple import config
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = config('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = config('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = config('MYSQL_HOST')
app.config['MYSQL_DB'] = config('MYSQL_DB')

mysql = MySQL(app)
