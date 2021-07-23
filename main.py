import io
import csv
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)