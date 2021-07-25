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

@app.route('/pesquisa')
def pesquisa():
	return render_template('pesquisa.html')

@app.route('/cadastro',methods = ['GET','POST'])
def formulario_cadastro():
	if request.method == 'POST':
		name = request.form['firstname']
		email = request.form['email']
		cpf = request.form['cpf']
		latitude = request.form['latitude']
		longitude = request.form['longitude']
		tipo_lavoura = request.form['lavoura']
		data = request.form['data']
		ocorrencia = request.form['ocorrencia']

		insert_query = '''INSERT INTO comunicaPerda VALUES(''' + '''
		0,''' + '"' + name + '",' + '"' + email + '",' + '"' + cpf + '",' + '''
		"''' + latitude + '",' + '"' + longitude + '",' + '"' + tipo_lavoura + '",' + '''
		" ''' + data + '",' + '"' + ocorrencia + '")'

		cursor.execute(insert_query)
		conn.commit()
		return render_template('index.html')

	return render_template('cadastro.html')


if __name__ == '__main__':
	app.run(debug=True)