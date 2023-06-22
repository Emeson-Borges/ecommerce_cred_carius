    class Funcoes{

        validaCPF(cpf) {
            cpf = cpf.replace(/[^\d]+/g, '');

    // Verificar se o CPF possui 11 dígitos
            if (cpf.length !== 11) {
                return false;
            }

            // Verificar se todos os dígitos são iguais
            if (/^(\d)\1+$/.test(cpf)) {
                return false;
            }

            // Validar os dígitos verificadores
            var soma = 0;
            var resto;
            for (var i = 1; i <= 9; i++) {
                soma = soma + parseInt(cpf.substring(i - 1, i)) * (11 - i);
            }
            resto = (soma * 10) % 11;

            if (resto === 10 || resto === 11) {
                resto = 0;
            }

            if (resto !== parseInt(cpf.substring(9, 10))) {
                return false;
            }

            soma = 0;
            for (var i = 1; i <= 10; i++) {
                soma = soma + parseInt(cpf.substring(i - 1, i)) * (12 - i);
            }
            resto = (soma * 10) % 11;

            if (resto === 10 || resto === 11) {
                resto = 0;
            }

            if (resto !== parseInt(cpf.substring(10, 11))) {
                return false;
            }

            return true;
            }
    }

    export default Funcoes
