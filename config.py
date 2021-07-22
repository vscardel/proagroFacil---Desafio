#documento com todos os imports e parametros necessarios

from flask import Flask,render_template,request,redirect,flash,session
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'vscardel'
app.config['MYSQL_DATABASE_PASSWORD'] = 'vC#33672324'
app.config['MYSQL_DATABASE_DB'] = 'proagroFacil'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['SECRET_KEY'] = '12345'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()