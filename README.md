# proagroFacil

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

**Deploy**: Este desafio está em https://proagrofacil.herokuapp.com/. O funcionamento não é perfeito pois o servidor se encontra muitas vezes indisponível, então **não é recomendado testar a aplicação por esse link, e sim pelo prório localhost.**
