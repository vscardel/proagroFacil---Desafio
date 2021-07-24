list_of_commom_valid_domains = ['gmail','hotmail','yahoo','aol','msn',
'mail','uol','ig','outlook'];

list_of_commom_valid_tld = ['com','net','org','gov','edu','info','mil'];

list_of_valid_events = ['CHUVA EXCESSIVA', 'GEADA', 'GRANIZO', 'SECA', 'VENDAVAL', 'RAIO'];

//checa se uma string eh composta pelo mesmo caractere
function check_same_char(my_str) {
	let first_char = my_str[0];
	for(let i=1; i < my_str.length; i++) {
		if(my_str[i] != first_char) {
			return false;
		}
	}
	return true;
}

//segue o algoritmo padrão de verificação de cpf
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
function validate_email(e) {
	email = document.getElementById('femail').value;
	console.log(email);
	if(email.length > 255) {
		return false;
	}
	console.log(email.length);
	let domain = "";
	let cont_arroba = 0;
	let tld = "";
	let cont_ponto = 0;
	//escaneia a string e separa o domain do tld
	for(let i=0;i<email.length; i++) {
		if(email[i] == '@') {
			cont_arroba += 1;
		}
		if(email[i] == '.') {
			cont_ponto += 1;
		}
		if(cont_arroba == 1 && cont_ponto == 0) {
			//primeiro @ encontrado
			if(email[i] == '@')
				continue;
			domain += email[i];
		}
		if(cont_ponto == 1) {
			//primeiro ponto encontrado
			if(email[i] == '.')
				continue;
			tld += email[i];
		}
	}
	if(list_of_commom_valid_domains.includes(domain) && 
		list_of_commom_valid_tld.includes(tld)) {
		return true;
	}
	else {
		return false;
	}
	
}

//determina se o evento digitado é válido
function validate_event(e) {
	event = document.getElementById('focorr').value;
	if(list_of_valid_events.includes(event)) {
		return true;
	}
	return false;
}

function validate_form(e) {
	name = document.getElementById('fname');
	email = document.getElementById('femail');
	cpf = document.getElementById('fcpf');
	lat = document.getElementById('flat');
	long = document.getElementById('flong');
	lavoura = document.getElementById('flav');
	ocorrencia = document.getElementById('focorr');
	date = document.getElementById('fdate');
	list_of_form_inputs = [name,email,cpf,lat,long,lavoura,ocorrencia,date]
	//assume q nao ocorreram erros
	let flag_input_error = true;
	for (input in list_of_form_inputs) {
		console.log(input.value);
		//if (input.value == '') {
			//borda do input setada como vermelha para indicar erro
		//	input.style.borderColor = "rgb(236, 19, 19)";
		//	flag_input_error = false;
		//}
	}
	//validação de email e cpf
	bool_cpf = validate_cpf();
	bool_email = validate_email();
	if(bool_cpf == false) {
		cpf.style.borderColor = "rgb(236, 19, 19)";
		flag_input_error = false;
	}
	if(bool_email == false) {
		email.style.borderColor = "rgb(236, 19, 19)";
		flag_input_error = false;
	}
	return flag_input_error;
}

function validate(e) {
	e.preventDefault();
	val_form = validate_form();
	alert(val_form);
}