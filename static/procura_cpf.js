// seleciona o cpf desejado escondendo os cpfs não desejados
// na tabela

function procuraPorCPF(){
	cpf = document.getElementById('fProcuraCPF');
	if(cpf.value == "") {
		alert("Digite o CPF");
		return;
	}
	linhas = document.getElementsByTagName('tr');
	flag_find = false;
	for(let i=0;i<linhas.length;i++) {
		let colunas = linhas[i].getElementsByTagName('td');
		//cpf
		if(colunas[1]){
			if(colunas[1].textContent.trim() != cpf.value){
				linhas[i].style.display = "none";  
			}
			else {
				if(linhas[i].style.display == "none") {
					linhas[i].style.display = "table-row"; 
				}
				flag_find = true;
			}
		}
	}
	if(!flag_find) {
		alert("CPF informado não existe na base de dados");
		//retorna as linhas que foram escondidas pela checagem
		//anterior
		for(let i=0;i<linhas.length;i++) {
			linhas[i].style.display = "table-row";  	
		}
	}

	botao_recarrega = document.getElementById('refresh_pesquisa');
	botao_recarrega.style.display = "inline";
}

