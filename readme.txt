Pré requisitos: Ler o arquivo requirements.txt

Deploy: Este desafio está em ... o resto do documento descreve aspectos técnicos e como preparar o ambiente para rodar o código no localhost caso assim se deseje.

Banco de Dados:
	
	1) O banco escolhido foi o MySQL
	2) Para conectar com o banco é necessário criá-lo. Para isso, basta seguir as próximas etapas.
		2.1) logue no MySQL: mysql -u 'username' -p 'password'
		2.2) crie a base: CREATE DATABASE proagroFacil;
		2.3) Selecione a base: USE proagroFacil;
		2.4) Copie e cole no terminal o código de criação das tabelas do arquivo /tables.sql
		2.5) No arquivo /config.py atribuir os valores corretos aos seguintes parâmetros:
			app.config['MYSQL_DATABASE_USER'] = 'username'
			app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
			app.config['MYSQL_DATABASE_DB'] = 'proagroFacil'
			app.config['MYSQL_DATABASE_HOST'] = 'localhost'
			app.config['SECRET_KEY'] = '12345'

			onde 'username' e 'password' são os mesmos parametros utilizados para logar no MySQL.

	O banco consiste de uma única tabela como descrita no documento do desafio. A chave primária é o CPF do produtor.

Rodando o código:
	No diretório do projeto, basta rodar o seguinte comando:
	Python3 app.py
	Daí é so entrar em localhost:5000 no navegador de sua preferência e utilizar o aplicativo.