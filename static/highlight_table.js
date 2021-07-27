//deixa a linha vermelha ou verde de acordo
//com o valor de suspeita da ocorrencia
function highlight_table(){
	linhas = document.getElementsByTagName('tr');
	for(let i=0;i<linhas.length;i++) {
		let colunas = linhas[i].getElementsByTagName('td');
		//SIM OU NAO
		if(colunas[6]){
			if(colunas[6].textContent.trim() == "SIM"){
				linhas[i].style.backgroundColor = "#7b8494";
			}
			else if(colunas[6].textContent.trim() == "NÃO") {
				linhas[i].style.backgroundColor = "#49a2f5";
			}
		}
	}
}