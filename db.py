from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b235ccdfe9b68f'
app.config['MYSQL_DATABASE_PASSWORD'] = '2a032b91'
app.config['MYSQL_DATABASE_DB'] = 'heroku_ca53e8cabd3c7ad'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-04.cleardb.com'
mysql.init_app(app)