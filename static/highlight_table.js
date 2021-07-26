//deixa a linha vermelha ou verde de acordo
//com o valor de suspeita da ocorrencia
function highlight_table(){
	linhas = document.getElementsByTagName('tr');
	for(let i=0;i<linhas.length;i++) {
		let colunas = linhas[i].getElementsByTagName('td');
		//SIM OU NAO
		if(colunas[6]){
			if(colunas[6].textContent.trim() == "SIM"){
				linhas[i].style.backgroundColor = "rgba(203,30,90,0.5)";
			}
			else if(colunas[6].textContent.trim() == "NÃO") {
				linhas[i].style.backgroundColor = "rgba(143,202,124,0.5)";
			}
		}
	}
}