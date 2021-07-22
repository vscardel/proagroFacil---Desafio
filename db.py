from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b7a0d73d0e0c21'
app.config['MYSQL_DATABASE_PASSWORD'] = '597fa7a7'
app.config['MYSQL_DATABASE_DB'] = 'heroku_c48710de58032a8'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-04.cleardb.com'
mysql.init_app(app)
