import io
import csv
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template,request,url_for

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cadastro',methods = ['GET','POST'])
def formulario_cadastro():
	if request.method == 'POST':
		return redirect(url_for('index'))
	return redirect(url_for('cadastro'))

if __name__ == '__main__':
	app.run(debug=True)