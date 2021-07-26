// seleciona o cpf desejado escondendo os cpfs não desejados
// na tabela


function procuraPorCPF(){
	cpf = document.getElementById('fProcuraCPF');
	if(cpf.value == "") {
		alert("Digite o CPF");
		return;
	}
	linhas = document.getElementsByTagName('tr');
	for(let i=0;i<linhas.length;i++) {
		let colunas = linhas[i].getElementsByTagName('td');
		//cpf
		if(colunas[1]){
			if(colunas[1].textContent.trim() != cpf.value){
				linhas[i].style.display = "none";  
			}
		}
	}
}

