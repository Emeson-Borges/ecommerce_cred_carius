const cidadesPorEstado = {
    acre: ["Rio Branco", "Cruzeiro do Sul", "Sena Madureira"],
    alagoas: ["Maceió", "Arapiraca", "Palmeira dos Índios"],
    amapa: ["Macapá", "Santana", "Laranjal do Jari"],
    amazonas: ["Manaus", "Parintins", "Itacoatiara"],
    bahia: ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    ceara: ["Fortaleza", "Juazeiro do Norte", "Caucaia"],
    "distrito-federal": ["Brasília"],
    "espirito-santo": ["Vitória", "Vila Velha", "Cariacica"],
    goias: ["Goiânia", "Aparecida de Goiânia", "Anápolis"],
    maranhao: ["São Luís", "Imperatriz", "Timon"],
    "mato-grosso": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
    "mato-grosso-do-sul": ["Campo Grande", "Dourados", "Três Lagoas"],
    "minas-gerais": ["Belo Horizonte", "Uberlândia", "Contagem"],
    para: ["Belém", "Ananindeua", "Santarém"],
    paraiba: ["João Pessoa", "Campina Grande", "Santa Rita"],
    parana: ["Curitiba", "Londrina", "Maringá"],
    pernambuco: ["Recife", "Jaboatão dos Guararapes", "Olinda"],
    piaui: ["Teresina", "Parnaíba", "Picos"],
    "rio-de-janeiro": ["Rio de Janeiro", "São Gonçalo", "Duque de Caxias"],
    "rio-grande-do-norte": ["Natal", "Mossoró", "Parnamirim"],
    "rio-grande-do-sul": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
    rondonia: ["Porto Velho", "Ji-Paraná", "Ariquemes"],
    roraima: ["Boa Vista", "Rorainópolis", "Caracaraí"],
    "santa-catarina": ["Florianópolis", "Joinville", "Blumenau"],
    "sao-paulo": ["São Paulo", "Guarulhos", "Campinas"],
    sergipe: ["Aracaju", "Nossa Senhora do Socorro", "Lagarto"],
    tocantins: ["Palmas", "Araguaína", "Gurupi"]
  };
  

const selectEstado = document.querySelector('select[name="estado"]');
const selectCidade = document.querySelector('select[name="cidade"]');

selectEstado.addEventListener('change', function() {
  const estadoSelecionado = this.value;
  
  // Limpa as opções do dropdown de cidades
  selectCidade.innerHTML = '<option selected disabled class="form_select_option" value="">Selecione</option>';
  
  // Verifica se um estado foi selecionado
  if (estadoSelecionado) {
    const cidades = cidadesPorEstado[estadoSelecionado];
    
    // Adiciona as opções de cidades no dropdown correspondente
    cidades.forEach((cidade) => {
      const optionElement = document.createElement('option');
      optionElement.textContent = cidade;
      optionElement.value = cidade;
      selectCidade.appendChild(optionElement);
    });
  }
});


function formatarRG(input){
    
  input.maxLength   = 12
  var rg            = input.value;

rg = rg.replace(/\D/g, "");

if (rg.length > 2) {
  rg = rg.substring(0, 2) + "." + rg.substring(2);
}
if (rg.length > 6) {
  rg = rg.substring(0, 6) + "." + rg.substring(6);
}
if (rg.length > 10) {
  rg = rg.substring(0, 10) + "-" + rg.substring(10);
}

input.value = rg;
}

function removerPontuacaoRG(rg) {
  return rg.replace(/[^\d]/g, "");
}

function validarRG() {
  const inputRg = document.getElementById("rg").value;
  const rgSemPontuacao = inputRg.replace(/\D/g, '');

  if (rgSemPontuacao.length !== 9) {
    alert("RG inválido. Deve conter exatamente 9 dígitos.");
    return;
  }

  const numeroRG = rgSemPontuacao.slice(0, 8);
  const digitoConf = rgSemPontuacao.slice(8);

  // Cálculo do dígito de confirmação
  let soma = 0;
  for (let i = 0; i < 8; i++) {
    soma += parseInt(numeroRG[i]) * (8 - i);
  }
  const resto = soma % 11;
  const digitoCalculado = resto < 2 ? 0 : 11 - resto;

  if (digitoCalculado === parseInt(digitoConf)) {
    return true
  } else {
    return false
  }
}
//Função para validar CPF
function validaCpf(cpf) {
    cpf = cpf.replace(/[^\d]+/g, '');
    if (cpf == '') return false;
    if (cpf.length != 11 ||
        cpf == "00000000000" ||
        cpf == "11111111111" ||
        cpf == "22222222222" ||
        cpf == "33333333333" ||
        cpf == "44444444444" ||
        cpf == "55555555555" ||
        cpf == "66666666666" ||
        cpf == "77777777777" ||
        cpf == "88888888888" ||
        cpf == "99999999999")
        return false;
    add = 0;
    for (i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    add = 0;
    for (i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
    return true;
}

  const cpf             = document.getElementById('cpf')
  const botao_cadastrar = document.getElementById('cadastrar');
  const form_cadastrar  = document.querySelector('.form')
  const rg              = document.getElementById('rg')
  //Função para remover a mascara
  function removerMascaraCPF(cpf) {
  return String(cpf).replace(/\D/g, '');
}

//validando o cpf e removendo a máscara
  botao_cadastrar.addEventListener('click',()=>{
    event.preventDefault();
    if(validaCpf(cpf.value)){
      if(validarRG == true){
        rg.value  = removerPontuacaoRG(rg.value)
        cpf.value = removerMascaraCPF(cpf.value)
        form_cadastrar.submit(); 
      }else{
        alert("RG Inválido")
      }
    }else{
      alert("CPF Inválido!")
    }
    
  })
  // Função para formatar a data de nascimento
  function formatarNascimento(input) {
  // Remove todos os caracteres que não sejam dígitos
  var valor = input.value.replace(/\D/g, '');

  // Verifica se o valor é uma data válida
  if (valor.length > 2) {
    // Insere a barra depois do dia
    valor = valor.replace(/^(\d{2})(\d)/, '$1/$2');
  }

  if (valor.length > 5) {
    // Insere a barra depois do mês
    valor = valor.replace(/^(\d{2})\/(\d{2})(\d)/, '$1/$2/$3');
  }

  // Atualiza o valor do campo de entrada
  if (input.value != null){
     input.value = valor;
  }
 
}
//Enquanto o usuário digitar ele formata a data
window.addEventListener("DOMContentLoaded", (event) => {
  let dataNascimento = document.getElementById('dtnasc_func')
  dataNascimento.addEventListener('input',()=>{
    formatarNascimento(dataNascimento)
})
});
//Formatar CPF
function formataCPF(input) {
  // Remove todos os caracteres que não sejam dígitos
  var valor = input.value.replace(/\D/g, '');

  // Adiciona os pontos de separação e o traço do CPF
  valor = valor.replace(/^(\d{3})(\d)/, '$1.$2');
  valor = valor.replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3');
  valor = valor.replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d{1,2})/, '$1.$2.$3-$4');

  // Atualiza o valor do campo de entrada
  input.value = valor;
}
//Enquanto o usuário digitar ele irá formatar o cpf
cpf.addEventListener('input', function() {
  formataCPF(this);
});


rg.addEventListener('input',()=>{
  console.log('formatando')
  formatarRG(rg)
})

window.onload = (event)=>{
    let estado = document.getElementById('estado').value
    selectEstado.value  = estado
      const cidades = cidadesPorEstado[estado];
      let city = document.getElementById('cidade').value
      // Adiciona as opções de cidades no dropdown correspondente
      cidades.forEach((cidade) => {
        const optionElement = document.createElement('option');
        optionElement.textContent = cidade;
        optionElement.value = cidade;
        selectCidade.appendChild(optionElement);
        if(city==cidade){
          optionElement.selected = true
        }
      });
      let cpf = document.getElementById('cpf')
      formataCPF(cpf);
    }
  
campos = document.querySelectorAll('.form-error')

campos.forEach(function(campo) {
  campo.addEventListener('input', function() {
    if (campo.value != ""){
      campo.style.backgroundColor = "#DCDCDC"
    }else{
      campo.style.backgroundColor = "rgb(252, 143, 179)"
    }
   
  });

});