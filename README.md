# proagroFacil


**Deploy**: Este desafio está em https://proagrofacil.herokuapp.com/. Ele foi hospedado utilizando a plataforma Heroku.

**Assume-se acesso a um terminal de algum SO unix-like**

**Pré requisitos**: em  /proagroFacil rode o comando _pip3 -r requirements.txt_
 
**Banco de Dados**:	
* O banco escolhido foi o MySQL  
* Para conectar com o banco é necessário criá-lo. Para isso, basta seguir as próximas etapas:  
  * logue no MySQL: mysql -u 'username' -p 'password'  
  * crie a base: CREATE DATABASE proagroFacil;  
  * Selecione a base: USE proagroFacil;  
  * Copie e cole no terminal o código de criação das tabelas do arquivo /proagroFacil/comunicaPerda.sql  
  * No arquivo /proagroFacil/db.py atribuir os valores corretos aos seguintes parâmetros:
    * app.config['MYSQL_DATABASE_USER'] = 'username'  
    * app.config['MYSQL_DATABASE_PASSWORD'] = 'password'  
    * app.config['MYSQL_DATABASE_DB'] = 'proagroFacil'  
    * app.config['MYSQL_DATABASE_HOST'] = 'localhost'  
    * app.config['SECRET_KEY'] = '12345'  
  * onde 'username' e 'password' são os mesmos parametros utilizados para logar no MySQL.  

**Rodando o código**:
* Em /proagroFacil, basta rodar o seguinte comando:
* _Python3 main.py_
* Daí é so entrar em localhost:5000 no navegador de sua preferência e utilizar o aplicativo.

**Considerações acerca da ocorrência suspeita**
* Em relação às ocorrências suspeitas, a decisão foi de avisar ao analista e armazenar no banco com uma flag de suspeita. A ocorrência é visualzada na tabela com uma cor distinta de ocorrências não suspeitas. O pensamento por trás dessa decisão é que cabe ao analista, após verificar a situação, decidir se a ocorrência precisa ser revista ou deletada.
