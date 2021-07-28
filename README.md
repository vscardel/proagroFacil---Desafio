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
* Outra decisão que precisou ser tomada foi se todas as ocorrências no mesmo dia que atendessem os critérios seriam marcadas como suspeitas ou apenas a ocorrência cadastrada. Se optou pela segunda opção, com as ocorrências dos outros dias se mantendo como não suspeitas.
* Pode acontecer da atualização de uma ocorrência torná-la suspeita. Por isso, no momento da atualização, a verificação de ocorrência suspeita é feita novamente e se a ocorrência se tornar suspeita ela será marcada como tal.
* Uma consequência dos pontos 1 e 2 é que uma ocorrência não suspeita pode ser atualizada em algum campo e ser marcada como suspeita pelo sistema, mesmo que o campo atualizado não tenha a ver com latitude, longitude e ocorrência. Isso acontece pois ela ocorreu no mesmo dia e em uma raio menor do que 10km de uma ocorrência marcada como suspeita anteriormente (com ocorrência divergente), e o sistema agora no momento da atualização verificou que ela é também suspeita. (por causa da verificação do segundo ponto). Isso não foi considerado um erro, e sim uma consequência das decisões tomadas.
