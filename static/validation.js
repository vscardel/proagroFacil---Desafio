list_of_commom_valid_domains = ['gmail','hotmail','yahoo,','aol','msn',
'mail','uol','ig''outlook'];

list_of_commom_valid_tld = ['com','net','org','gov','edu','info','mil'];

list_of_valid_events = ['CHUVA EXCESSIVA', 'GEADA', 'GRANIZO', 'SECA', 'VENDAVAL', 'RAIO'];

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
	let cpf = document.getElementById('fcpf').value;
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
		for(let i=0;i<9;i++) {
			sum += (cont*parseInt(cpf[i]));
			cont--;
		}
		let first_verification_result = (sum*10) % 11;
		if(first_verification_result == 10) {
			first_verification_result = 0.
		}
		if(first_verification_result != first_digit) {
			return false;
		}
		//verificacao do primeiro digito
		cont = 11;
		sum = 0;
		for(let i=0;i<10;i++) {
			sum += (cont*parseInt(cpf[i]));
			cont--;
		}
		let second_verification_result = (sum*10) % 11;
		if(second_verification_result == 10) {
			second_verification_result = 0;
		}
		if(second_verification_result != second_digit) {
			return false;
		}
		return true;
	}
}

//simplificações: checa por dominios e TLDs mais comuns.
//se nenhum bater, retorna false. Não será verificado se
//a parte local do endereço de e-mail é válida para evitar
//o uso de regex e verificações muito complicadas
function validade_email(e) {
	email = document.getElementById('femail').value;
	let domain = "";
	let flag_domain = false;
	let tld = "";
	let flag_tld = false;
	for(let i=0;i<email.length; i++) {
		if(email[i] == '@') {
			flag_domain = true;
		}
		else if(email[i] == '.') {
			flag_tld = true;
			flag_domain = false;
		}
		if(flag_domain) {
			domain += email[i];
		}
		if(flag_tld) {
			tld += email[i];
		}
	}
	console.log(domain);
	console.log(tld);
}

function debug(e) {
	e.preventDefault();
	validade_email();
	return false;
}