from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'ba53f59ae43488'
app.config['MYSQL_DATABASE_PASSWORD'] = '38b64338'
app.config['MYSQL_DATABASE_DB'] = 'heroku_8ab7278552ae92f'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-04.cleardb.com'
mysql.init_app(app)
