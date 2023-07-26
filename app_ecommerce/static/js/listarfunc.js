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
  
  function formatarNascimento() {
    pesquisa.placeholder = 'DD/MM/AAAA'
    pesquisa.maxLength   = 10
    // Remove todos os caracteres que não sejam dígitos
    var valor = pesquisa.value.replace(/\D/g, '');
  
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
    if (pesquisa.value != null){
       pesquisa.value = valor;
    }

    isRGFormated   = false
    isDateFormated = true
    isCPfFormated  = false
  }

  function formatarTabelaRG(rg) {
    console.log("Formatando RG")
    // Separando o número do dígito de confirmação
    const numeroRG = rg.textContent.slice(0, 8);
    const digitoConf = rg.textContent.slice(8);
  
    // Formatando com pontuação
    rg.textContent = `${numeroRG.substr(0, 2)}.${numeroRG.substr(2, 3)}.${numeroRG.substr(5, 3)}-${digitoConf}`;
    console.log(rg.textContent)
  }
  
  function formataCPF(event) {
    pesquisa.placeholder="XXX.XXX.XXX-XX"
    pesquisa.maxLength  = 14
    // Remove todos os caracteres que não sejam dígitos
    var valor = pesquisa.value.replace(/\D/g, '');
  
    // Adiciona os pontos de separação e o traço do CPF
    valor = valor.replace(/^(\d{3})(\d)/, '$1.$2');
    valor = valor.replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3');
    valor = valor.replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d{1,2})/, '$1.$2.$3-$4');
  
    // Atualiza o valor do campo de entrada
    pesquisa.value = valor;

    isRGFormated   = false
    isDateFormated = false
    isCPfFormated  = true
  }

  function formataCPFTabela(celula) {
    console.log("Formatando celula")
    celula.textContent = celula.textContent.replace(/^(\d{3})(\d{3})(\d{3})(\d{2})$/, '$1.$2.$3-$4');
  }

  function formatarRG(event){
    
    pesquisa.maxLength   = 12
    var rg = pesquisa.value;

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

  pesquisa.value = rg;
  isRGFormated   = true
  isCPfFormated  = false 
  isDateFormated = false
}

  function removerMascaraCPF(cpf) {
    return String(cpf).replace(/\D/g, '');
  }

  function removerPontuacaoRG(rg) {
    return rg.replace(/[^\d]/g, "");
  }

  
const selectEstado         = document.querySelector('select[name="estado"]');
const selectCidade         = document.querySelector('select[name="cidade"]');
const tipo_pesquisa        = document.querySelectorAll('input[name="tipo_pesquisa"]')
const selecionado          = document.querySelector('input[name="tipo_pesquisa"]:checked')
const pesquisa             = document.querySelector('input[name="pesquisa"]')
let isCPfFormated          = false
let isRGFormated           = false
let isDateFormated         = false
let isTextSelected         = false
const cpfs                 = document.querySelectorAll('.cpf')
const rgs                  = document.querySelectorAll('.rg')

tipo_pesquisa.forEach((option)=>{
  option.addEventListener('change',()=>{
    if(option.value=="CPF"){
      pesquisa.placeholder = "XXX.XXX.XXX-XX"
      pesquisa.addEventListener('input',formataCPF)
  }else if(option.value=="RG"){
    pesquisa.placeholder = "XX.XXX.XXX-X"
    pesquisa.addEventListener('input',formatarRG)
  }else if(option.value=="Data de Nascimento"){
    pesquisa.placeholder="DD/MM/AAAA"
    pesquisa.addEventListener('input',formatarNascimento)
  }else if(option.value=="Texto"){
    pesquisa.placeholder="Digite sua pesquisa"
    console.log("Está sendo removido")
    if(isCPfFormated){
      pesquisa.removeEventListener('input',formataCPF)
    }
    if(isRGFormated){
      pesquisa.removeEventListener('input',formatarRG)
    }
    if(isDateFormated){
      console.log('Removendo mascara de data de nascimento')
      pesquisa.removeEventListener('input',formatarNascimento)
    }
  
  }

})
  
})


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
window.onload = (event)=>{
const form_pesquisa = document.getElementById('form-pesquisa')
form_pesquisa.addEventListener('submit',()=>{
 
  for (const tp of tipo_pesquisa) {
    console.log(tp.value)
    if(tp.checked){
      if (tp.value=="CPF") {
        pesquisa.value = removerMascaraCPF(pesquisa.value)
       }else if(tp.value=="RG"){
         pesquisa.value = removerPontuacaoRG(pesquisa.value)
       }
    }
    
  }
})

var linhas = document.querySelectorAll('.linha');
var cont = 1
  linhas.forEach(function(linha) {
    console.log(linha)
    if(cont %2  !=0){
      
      linha.style.backgroundColor = 'rgb(86, 183, 201)'
    }

    cont +=1
  });
;
 cpfs.forEach((cpf)=>{
  formataCPFTabela(cpf)
 })

 rgs.forEach((rg)=>{
  formatarTabelaRG(rg)
 })

}


const deletar = document.querySelectorAll('.btn-deletar')
deletar.forEach(function(botao){
  botao.addEventListener('click',()=>{
    event.preventDefault()
    const confirmacao = confirm('Deseja deletar?');
    console.log(confirmacao)
    if (confirmacao==true) {
      console.log('deletado')
      window.location.href = botao.href; 
    } 
  })
})
