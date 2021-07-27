from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'bcf54691a923ce'
app.config['MYSQL_DATABASE_PASSWORD'] = 'f26fd33d'
app.config['MYSQL_DATABASE_DB'] = 'heroku_42e6ce0de3a9265'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-04.cleardb.com'

mysql.init_app(app)
