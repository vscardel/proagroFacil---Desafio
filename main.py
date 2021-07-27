import io
import math
import csv
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template,request,url_for,redirect

conn = mysql.connect()
cursor = conn.cursor()

#maxima distancia permitida para que uma ocorrencia nao seja
#considerada suspeita de acordo com os critérios apresentados
max_dist = 10

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/pesquisa')
def pesquisa():
	return_todas_query = "SELECT * FROM comunicaPerda"
	cursor.execute(return_todas_query)
	todas_ocorrencias = cursor.fetchall()
	return render_template('pesquisa.html',
	todas_ocorrencias = todas_ocorrencias)

# Usa a fórmula de‘haversine’ para calcular a 
# distancia entre pontos na forma (lat,long) 
#d = R ⋅ c
#c = 2 ⋅ atan2( √a, √(1−a) )
#a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)

def calcula_distancia(lat1,lat2,long1,long2):
	#raio da terra em km
	R = 6371
	#math.pi/180 converte em radianos
	lat1_rad = lat1 * (math.pi/180)
	lat2_rad = lat2 * (math.pi/180)
	diff_lat = (lat2 - lat1) * (math.pi/180)
	diff_long = (long2 - long1) * (math.pi/180)
	a = math.sin(diff_lat/2)**2 + (math.cos(lat1_rad) \
		* math.cos(lat2_rad) * math.sin(diff_long/2)**2)
	c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
	return (R*c)

#retorna todas as ocorrencias que aconteceram na mesma data
#com suas latitudes e longidutes
def retorna_ocorrencias_mesma_data(data):
	ocorrencias_mesma_data_query = '''SELECT latitude,longitude,evento 
	FROM comunicaPerda''' + " WHERE data = " + '"' + data + '"'
	cursor.execute(ocorrencias_mesma_data_query)
	return cursor.fetchall()


def determina_ocorrencia_suspeita(lat_entrada,long_entrada,
	evento,ocorrencias_mesma_data):
	global max_dist
	for ocorrencia in ocorrencias_mesma_data:
		lat_ocorr = float(ocorrencia[0])
		long_ocorr = float(ocorrencia[1])
		dist = calcula_distancia(lat_entrada,lat_ocorr,
		long_entrada,long_ocorr)
		if(dist <= max_dist) and (str(ocorrencia[2]) != str(evento) ):
			return True
	return False

@app.route('/cadastro',methods = ['GET','POST'])
def formulario_cadastro():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		cpf = request.form['cpf']
		latitude = request.form['latitude']
		longitude = request.form['longitude']
		tipo_lavoura = request.form['lavoura']
		data = request.form['data']
		evento = request.form['ocorrencia']

		ocorrencias_mesma_data = retorna_ocorrencias_mesma_data(data)
		is_suspeita = determina_ocorrencia_suspeita(
			float(latitude), float(longitude),evento,ocorrencias_mesma_data)

		#insere 1 no campo de suspeita
		if is_suspeita:
			insert_query = '''INSERT INTO comunicaPerda VALUES(''' + "0," + '''
			1,''' + '"' + name + '",' + '"' + email + '",' + '"' + cpf + '",' + '''
			''' + str(float(latitude)) + ',' + str(float(longitude)) + ',' + '"' + tipo_lavoura + '",' + '''
			"''' + data + '",' + '"' + evento + '")'
			cursor.execute(insert_query)
			conn.commit()
			return render_template('cadastro.html',is_suspeita = is_suspeita)

		#insere 0 no campo de suspeita
		else:
			insert_query = '''INSERT INTO comunicaPerda VALUES(''' + "0," + '''
			0,''' + '"' + name + '",' + '"' + email + '",' + '"' + cpf + '",' + '''
			''' + str(float(latitude)) + ',' + str(float(longitude)) + ',' + '"' + tipo_lavoura + '",' + '''
			"''' + data + '",' + '"' + evento + '")'
			cursor.execute(insert_query)
			conn.commit()
			return redirect('/pesquisa')
		

	return render_template('cadastro.html')

@app.route('/delete/<int:id>')
def delete(id):
	delete_query = "DELETE FROM comunicaPerda WHERE id = " + str(id)
	cursor.execute(delete_query)
	conn.commit()
	return redirect('/pesquisa')

@app.route('/update/<int:id>', methods = ['GET','POST'])
def update(id):

	#com o intuito de deixar os valores antigos no formulário
	#para não precisar preencher todos os dados novamente
	get_old_values_query = "SELECT * FROM comunicaPerda WHERE id = " + str(id)
	cursor.execute(get_old_values_query)
	old_values = cursor.fetchall()

	if request.method == 'POST':

		name = request.form['name']
		email = request.form['email']
		cpf = request.form['cpf']
		latitude = request.form['latitude']
		longitude = request.form['longitude']
		tipo_lavoura = request.form['lavoura']
		print(tipo_lavoura)
		data = request.form['data']
		evento = request.form['ocorrencia']

		#necessario pois às vezes a atualização pode tornar a ocorrencia
		#suspeita
		ocorrencias_mesma_data = retorna_ocorrencias_mesma_data(data)
		is_suspeita = determina_ocorrencia_suspeita(
			float(latitude), float(longitude),evento,ocorrencias_mesma_data)

		if is_suspeita:
			update_query = '''UPDATE comunicaPerda
						SET nome = ''' + '"' + name + '",' + '''
						suspeito = 1 ''' + ',' + '''
						email = ''' + '"' + email + '",' + '''
						cpf = ''' + '"' + cpf + '",' + '''
						latitude = ''' + '"' + latitude + '",' + '''
						longitude = ''' + '"' + longitude + '",' +'''
						tipo = ''' + '"' + tipo_lavoura + '",' + '''
						data = ''' + '"' + data + '",'+ '''
						evento = ''' + '"' + evento + '"' + '''
						WHERE id = ''' + str(id)
			cursor.execute(update_query)
			conn.commit()
			return render_template('update.html',old_values = old_values,is_suspeita = is_suspeita)

		else:
			update_query = '''UPDATE comunicaPerda
						SET nome = ''' + '"' + name + '",' + '''
						suspeito = 0 ''' + ',' + '''
						email = ''' + '"' + email + '",' + '''
						cpf = ''' + '"' + cpf + '",' + '''
						latitude = ''' +  latitude + ',' + '''
						longitude = ''' + longitude + ',' +'''
						tipo = ''' + '"' + tipo_lavoura + '",' + '''
						data = ''' + '"' + data + '",'+ '''
						evento = ''' + '"' + evento + '"' + '''
						WHERE id = ''' + str(id)
			cursor.execute(update_query)
			conn.commit()
			return redirect('/pesquisa')

	return render_template('update.html',id = id, old_values = old_values)

if __name__ == '__main__':
	app.run(debug=False)