//checa se uma eh composta pelo mesmo caracter
function check_same_char(my_str) {
	let first_char = my_str[0];
	for(let i=1; i < my_str.length; i++) {
		if(my_str[i] != first_char) {
			return false;
		}
	}
	return true;
}

function validate_cpf(e) {
	let cpf = document.getElementById('fcpf');
	// tamanho invalido
	if(cpf.length != 11) {
		return false;
	}
	//cpf com os mesmos caracteres
	else if(check_same_char(cpf)) {
		return false;
	}
	else {
		//algoritmo de verificacao
		let first_digit = cpf[9];
		let second_digit = cpf[10];
		//verificacao do primeiro digito
		let cont = 10;
		let sum = 0;
		for(let i=0;i<10;i++) {
			sum += (cont*parseInt(cpf[i]));
			cont--;
		}
		let first_verification_result = (sum*10) % 11;
		if(first_verification_result != first_digit) {
			return false;
		}
		//verificacao do primeiro digito
		cont = 11;
		sum = 0;
		for(let i=0;i<11;i++) {
			sum += (cont*parseInt(cpf[i]));
			cont--;
		}
		let second_verification_result = (sum*10) % 11;
		if(second_verification_result != second_digit) {
			return false;
		}
		return true;
	}
}

function debug(e) {
	e.preventDefault();
	alert(validate_cpf());
	return false;
}