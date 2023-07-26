const cidadesPorEstado = {
    acre: ["Acrelândia",
          "Assis Brasil",
          "Brasiléia",
          "Bujari",
          "Capixaba",
          "Cruzeiro do Sul",
          "Epitaciolândia",
          "Feijó",
          "Jordão",
          "Mâncio Lima",
          "Manoel Urbano",
          "Marechal Thaumaturgo",
          "Plácido de Castro",
          "Porto Acre",
          "Porto Walter",
          "Rio Branco",
          "Rodrigues Alves",
          "Santa Rosa do Purus",
          "Sena Madureira",
          "Senador Guiomard",
          "Tarauacá",
          "Xapuri"],
    alagoas: ["Água Branca",
              "Anadia",
              "Arapiraca",
              "Atalaia",
              "Barra de Santo Antônio",
              "Barra de São Miguel",
              "Batalha",
              "Belém",
              "Belo Monte",
              "Boca da Mata",
              "Branquinha",
              "Cacimbinhas",
              "Cajueiro",
              "Campestre",
              "Campo Alegre",
              "Campo Grande",
              "Canapi",
              "Capela",
              "Carneiros",
              "Chã Preta",
              "Coité do Nóia",
              "Colônia Leopoldina",
              "Coqueiro Seco",
              "Coruripe",
              "Craíbas",
              "Delmiro Gouveia",
              "Dois Riachos",
              "Estrela de Alagoas",
              "Feira Grande",
              "Feliz Deserto",
              "Flexeiras",
              "Girau do Ponciano",
              "Ibateguara",
              "Igaci",
              "Igreja Nova",
              "Inhapi",
              "Jacaré dos Homens",
              "Jacuípe",
              "Japaratinga",
              "Jaramataia",
              "Jequiá da Praia",
              "Joaquim Gomes",
              "Jundiá",
              "Junqueiro",
              "Lagoa da Canoa",
              "Limoeiro de Anadia",
              "Maceió",
              "Major Isidoro",
              "Mar Vermelho",
              "Maragogi",
              "Maravilha",
              "Marechal Deodoro",
              "Maribondo",
              "Mata Grande",
              "Matriz de Camaragibe",
              "Messias",
              "Minador do Negrão",
              "Monteirópolis",
              "Murici",
              "Novo Lino",
              "Olho d'Água das Flores",
              "Olho d'Água do Casado",
              "Olho d'Água Grande",
              "Olivença",
              "Ouro Branco",
              "Palestina",
              "Palmeira dos Índios",
              "Pão de Açúcar",
              "Pariconha",
              "Paripueira",
              "Passo de Camaragibe",
              "Paulo Jacinto",
              "Penedo",
              "Piaçabuçu",
              "Pilar",
              "Pindoba",
              "Piranhas",
              "Poço das Trincheiras",
              "Porto Calvo",
              "Porto de Pedras",
              "Porto Real do Colégio",
              "Quebrangulo",
              "Rio Largo",
              "Roteiro",
              "Santa Luzia do Norte",
              "Santana do Ipanema",
              "Santana do Mundaú",
              "São Brás",
              "São José da Laje",
              "São José da Tapera",
              "São Luís do Quitunde",
              "São Miguel dos Campos",
              "São Miguel dos Milagres",
              "São Sebastião",
              "Satuba",
              "Senador Rui Palmeira",
              "Tanque d'Arca",
              "Taquarana",
              "Teotônio Vilela",
              "Traipu",
              "União dos Palmares",
              "Viçosa"],
    amapa:[
    "Amapá",
    "Calçoene",
    "Cutias",
    "Ferreira Gomes",
    "Itaubal",
    "Laranjal do Jari",
    "Macapá",
    "Mazagão",
    "Oiapoque",
    "Pedra Branca do Amapari",
    "Porto Grande",
    "Pracuúba",
    "Santana",
    "Serra do Navio",
    "Tartarugalzinho",
    "Vitória do Jari"
    ],
    amazonas: [ "Alvarães",
"Amaturá",
"Anamã",
"Anori",
"Apuí",
"Atalaia do Norte",
"Autazes",
"Barcelos",
"Barreirinha",
"Benjamin Constant",
"Beruri",
"Boa Vista do Ramos",
"Boca do Acre",
"Borba",
"Caapiranga",
"Canutama",
"Carauari",
"Careiro",
"Careiro da Várzea",
"Coari",
"Codajás",
"Eirunepé",
"Envira",
"Fonte Boa",
"Guajará",
"Humaitá",
"Ipixuna",
"Iranduba",
"Itacoatiara",
"Itamarati",
"Itapiranga",
"Japurá",
"Juruá",
"Jutaí",
"Lábrea",
"Manacapuru",
"Manaquiri",
"Manaus",
"Manicoré",
"Maraã",
"Maués",
"Nhamundá",
"Nova Olinda do Norte",
"Novo Airão",
"Novo Aripuanã",
"Parintins",
"Pauini",
"Presidente Figueiredo",
"Rio Preto da Eva",
"Santa Isabel do Rio Negro",
"Santo Antônio do Içá",
"São Gabriel da Cachoeira",
"São Paulo de Olivença",
"São Sebastião do Uatumã",
"Silves",
"Tabatinga",
"Tapauá",
"Tefé",
"Tonantins",
"Uarini",
"Urucará",
"Urucurituba"],
    bahia: ["Abaíra",
"Abaré",
"Acajutiba",
"Adustina",
"Água Fria",
"Aiquara",
"Alagoinhas",
"Alcobaça",
"Almadina",
"Amargosa",
"Amélia Rodrigues",
"América Dourada",
"Anagé",
"Andaraí",
"Andorinha",
"Angical",
"Anguera",
"Antas",
"Antônio Cardoso",
"Antônio Gonçalves",
"Aporá",
"Apuarema",
"Araças",
"Aracatu",
"Araci",
"Aramari",
"Arataca",
"Aratuípe",
"Aurelino Leal",
"Baianópolis",
"Baixa Grande",
"Banzaê",
"Barra",
"Barra da Estiva",
"Barra do Choça",
"Barra do Mendes",
"Barra do Rocha",
"Barreiras",
"Barro Alto",
"Barro Preto",
"Barrocas",
"Belmonte",
"Belo Campo",
"Biritinga",
"Boa Nova",
"Boa Vista do Tupim",
"Bom Jesus da Lapa",
"Bom Jesus da Serra",
"Boninal",
"Bonito",
"Boquira",
"Botuporã",
"Brejões",
"Brejolândia",
"Brotas de Macaúbas",
"Brumado",
"Buerarema",
"Buritirama",
"Caatiba",
"Cabaceiras do Paraguaçu",
"Cachoeira",
"Caculé",
"Caém",
"Caetanos",
"Caetité",
"Cafarnaum",
"Cairu",
"Caldeirão Grande",
"Camacan",
"Camaçari",
"Camamu",
"Campo Alegre de Lourdes",
"Campo Formoso",
"Canápolis",
"Canarana",
"Canavieiras",
"Candeal",
"Candeias",
"Candiba",
"Cândido Sales",
"Cansanção",
"Canudos",
"Capela do Alto Alegre",
"Capim Grosso",
"Caraíbas",
"Caravelas",
"Cardeal da Silva",
"Carinhanha",
"Casa Nova",
"Castro Alves",
"Catolândia",
"Catu",
"Caturama",
"Central",
"Chorrochó",
"Cícero Dantas",
"Cipó",
"Coaraci",
"Cocos",
"Conceição da Feira",
"Conceição do Almeida",
"Conceição do Coité",
"Conceição do Jacuípe",
"Conde",
"Condeúba",
"Contendas do Sincorá",
"Coração de Maria",
"Cordeiros",
"Coribe",
"Coronel João Sá",
"Correntina",
"Cotegipe",
"Cravolândia",
"Crisópolis",
"Cristópolis",
"Cruz das Almas",
"Curaçá",
"Dário Meira",
"Dias d'Ávila",
"Dom Basílio",
"Dom Macedo Costa",
"Elísio Medrado",
"Encruzilhada",
"Entre Rios",
"Érico Cardoso",
"Esplanada",
"Euclides da Cunha",
"Eunápolis",
"Fátima",
"Feira da Mata",
"Feira de Santana",
"Filadélfia",
"Firmino Alves",
"Floresta Azul",
"Formosa do Rio Preto",
"Gandu",
"Gavião",
"Gentio do Ouro",
"Glória",
"Gongogi",
"Governador Mangabeira",
"Guajeru",
"Guanambi",
"Guaratinga",
"Heliópolis",
"Iaçu",
"Ibiassucê",
"Ibicaraí",
"Ibicoara",
"Ibicuí",
"Ibipeba",
"Ibipitanga",
"Ibiquera",
"Ibirapitanga",
"Ibirapuã",
"Ibirataia",
"Ibitiara",
"Ibititá",
"Ibotirama",
"Ichu",
"Igaporã",
"Igrapiúna",
"Iguaí",
"Ilhéus",
"Inhambupe",
"Ipecaetá",
"Ipiaú",
"Ipirá",
"Ipupiara",
"Irajuba",
"Iramaia",
"Iraquara",
"Irará",
"Irecê",
"Itabela",
"Itaberaba",
"Itabuna",
"Itacaré",
"Itaeté",
"Itagi",
"Itagibá",
"Itagimirim",
"Itaguaçu da Bahia",
"Itaju do Colônia",
"Itajuípe",
"Itamaraju",
"Itamari",
"Itambé",
"Itanagra",
"Itanhém",
"Itaparica",
"Itapé",
"Itapebi",
"Itapetinga",
"Itapicuru",
"Itapitanga",
"Itaquara",
"Itarantim",
"Itatim",
"Itiruçu",
"Itiúba",
"Itororó",
"Ituaçu",
"Ituberá",
"Iuiú",
"Jaborandi",
"Jacaraci",
"Jacobina",
"Jaguaquara",
"Jaguarari",
"Jaguaripe",
"Jandaíra",
"Jequié",
"Jeremoabo",
"Jiquiriçá",
"Jitaúna",
"João Dourado",
"Juazeiro",
"Jucuruçu",
"Jussara",
"Jussari",
"Jussiape",
"Lafaiete Coutinho",
"Lagoa Real",
"Laje",
"Lajedão",
"Lajedinho",
"Lajedo do Tabocal",
"Lamarão",
"Lapão",
"Lauro de Freitas",
"Lençóis",
"Licínio de Almeida",
"Livramento de Nossa Senhora",
"Luís Eduardo Magalhães",
"Macajuba",
"Macarani",
"Macaúbas",
"Macururé",
"Madre de Deus",
"Maetinga",
"Maiquinique",
"Mairi",
"Malhada",
"Malhada de Pedras",
"Manoel Vitorino",
"Mansidão",
"Maracás",
"Maragogipe",
"Maraú",
"Marcionílio Souza",
"Mascote",
"Mata de São João",
"Matina",
"Medeiros Neto",
"Miguel Calmon",
"Milagres",
"Mirangaba",
"Mirante",
"Monte Santo",
"Morpará",
"Morro do Chapéu",
"Mortugaba",
"Mucugê",
"Mucuri",
"Mulungu do Morro",
"Mundo Novo",
"Muniz Ferreira",
"Muquém de São Francisco",
"Muritiba",
"Mutuípe",
"Nazaré",
"Nilo Peçanha",
"Nordestina",
"Nova Canaã",
"Nova Fátima",
"Nova Ibiá",
"Nova Itarana",
"Nova Redenção",
"Nova Soure",
"Nova Viçosa",
"Novo Horizonte",
"Novo Triunfo",
"Olindina",
"Oliveira dos Brejinhos",
"Ouriçangas",
"Ourolândia",
"Palmas de Monte Alto",
"Palmeiras",
"Paramirim",
"Paratinga",
"Paripiranga",
"Pau Brasil",
"Paulo Afonso",
"Pé de Serra",
"Pedrão",
"Pedro Alexandre",
"Piatã",
"Pilão Arcado",
"Pindaí",
"Pindobaçu",
"Pintadas",
"Piraí do Norte",
"Piripá",
"Piritiba",
"Planaltino",
"Planalto",
"Poções",
"Pojuca",
"Ponto Novo",
"Porto Seguro",
"Potiraguá",
"Prado",
"Presidente Dutra",
"Presidente Jânio Quadros",
"Presidente Tancredo Neves",
"Queimadas",
"Quijingue",
"Quixabeira",
"Rafael Jambeiro",
"Remanso",
"Retirolândia",
"Riachão das Neves",
"Riachão do Jacuípe",
"Riacho de Santana",
"Ribeira do Amparo",
"Ribeira do Piauí",
"Ribeira do Rio Pardo",
"Ribeirão do Largo",
"Ribeirão do Salto",
"Rio de Contas",
"Rio do Antônio",
"Rio do Pires",
"Rio Real",
"Rodelas",
"Ruy Barbosa",
"Salinas da Margarida",
"Salvador",
"Santa Bárbara",
"Santa Brígida",
"Santa Cruz Cabrália",
"Santa Cruz da Vitória",
"Santa Inês",
"Santa Luzia",
"Santa Maria da Vitória",
"Santa Rita de Cássia",
"Santa Teresinha",
"Santaluz",
"Santana",
"Santanópolis",
"Santo Amaro",
"Santo Antônio de Jesus",
"Santo Estêvão",
"São Desidério",
"São Domingos",
"São Felipe",
"São Félix",
"São Félix do Coribe",
"São Francisco do Conde",
"São Gabriel",
"São Gonçalo dos Campos",
"São José da Vitória",
"São José do Jacuípe",
"São Miguel das Matas",
"São Sebastião do Passé",
"Sapeaçu",
"Sátiro Dias",
"Saubara",
"Saúde",
"Seabra",
"Sebastião Laranjeiras",
"Senhor do Bonfim",
"Sento Sé",
"Serra do Ramalho",
"Serra Dourada",
"Serra Preta",
"Serrinha",
"Serrolândia",
"Simões Filho",
"Sítio do Mato",
"Sítio do Quinto",
"Sobradinho",
"Souto Soares",
"Tabocas do Brejo Velho",
"Tanhaçu",
"Tanque Novo",
"Tanquinho",
"Taperoá",
"Tapiramutá",
"Teixeira de Freitas",
"Teodoro Sampaio",
"Teofilândia",
"Teolândia",
"Terra Nova",
"Tremedal",
"Tucano",
"Uauá",
"Ubaíra",
"Ubaitaba",
"Ubatã",
"Uibaí",
"Umburanas",
"Una",
"Urandi",
"Uruçuca",
"Utinga",
"Valença",
"Valente",
"Várzea da Roça",
"Várzea do Poço",
"Várzea Nova",
"Varzedo",
"Vera Cruz",
"Vereda",
"Vitória da Conquista",
"Wagner",
"Wanderley",
"Wenceslau Guimarães",
"Xique-Xique"],
    ceara: ["Abaiara",
            "Acarape",
            "Acaraú",
            "Acopiara",
            "Aiuaba",
            "Alcântaras",
            "Altaneira",
            "Alto Santo",
            "Amontada",
            "Antonina do Norte",
            "Apuiarés",
            "Aquiraz",
            "Aracati",
            "Aracoiaba",
            "Ararendá",
            "Araripe",
            "Aratuba",
            "Arneiroz",
            "Assaré",
            "Aurora",
            "Baixio",
            "Banabuiú",
            "Barbalha",
            "Barreira",
            "Barro",
            "Barroquinha",
            "Baturité",
            "Beberibe",
            "Bela Cruz",
            "Boa Viagem",
            "Brejo Santo",
            "Camocim",
            "Campos Sales",
            "Canindé",
            "Capistrano",
            "Caridade",
            "Cariré",
            "Caririaçu",
            "Cariús",
            "Carnaubal",
            "Cascavel",
            "Catarina",
            "Catunda",
            "Caucaia",
            "Cedro",
            "Chaval",
            "Choró",
            "Chorozinho",
            "Coreaú",
            "Crateús",
            "Crato",
            "Croatá",
            "Cruz",
            "Deputado Irapuan Pinheiro",
            "Ererê",
            "Eusébio",
            "Farias Brito",
            "Forquilha",
            "Fortaleza",
            "Fortim",
            "Frecheirinha",
            "General Sampaio",
            "Graça",
            "Granja",
            "Granjeiro",
            "Groaíras",
            "Guaiúba",
            "Guaraciaba do Norte",
            "Guaramiranga",
            "Hidrolândia",
            "Horizonte",
            "Ibaretama",
            "Ibiapina",
            "Ibicuitinga",
            "Icapuí",
            "Icó",
            "Iguatu",
            "Independência",
            "Ipaporanga",
            "Ipaumirim",
            "Ipu",
            "Ipueiras",
            "Iracema",
            "Irauçuba",
            "Itaiçaba",
            "Itaitinga",
            "Itapagé",
            "Itapipoca",
            "Itapiúna",
            "Itarema",
            "Itatira",
            "Jaguaretama",
            "Jaguaribara",
            "Jaguaribe",
            "Jaguaruana",
            "Jardim",
            "Jati",
            "Jijoca de Jericoacoara",
            "Juazeiro do Norte",
            "Jucás",
            "Lavras da Mangabeira",
            "Limoeiro do Norte",
            "Madalena",
            "Maracanaú",
            "Maranguape",
            "Marco",
            "Martinópole",
            "Massapê",
            "Mauriti",
            "Meruoca",
            "Milagres",
            "Milhã",
            "Miraíma",
            "Missão Velha",
            "Mombaça",
            "Monsenhor Tabosa",
            "Morada Nova",
            "Moraújo",
            "Morrinhos",
            "Mucambo",
            "Mulungu",
            "Nova Olinda",
            "Nova Russas",
            "Novo Oriente",
            "Ocara",
            "Orós",
            "Pacajus",
            "Pacatuba",
            "Pacoti",
            "Pacujá",
            "Palhano",
            "Palmácia",
            "Paracuru",
            "Paraipaba",
            "Parambu",
            "Paramoti",
            "Pedra Branca",
            "Penaforte",
            "Pentecoste",
            "Pereiro",
            "Pindoretama",
            "Piquet Carneiro",
            "Pires Ferreira",
            "Poranga",
            "Porteiras",
            "Potengi",
            "Potiretama",
            "Quiterianópolis",
            "Quixadá",
            "Quixelô",
            "Quixeramobim",
            "Quixeré",
            "Redenção",
            "Reriutaba",
            "Russas",
            "Saboeiro",
            "Salitre",
            "Santa Quitéria",
            "Santana do Acaraú",
            "Santana do Cariri",
            "São Benedito",
            "São Gonçalo do Amarante",
            "São João do Jaguaribe",
            "São Luís do Curu",
            "Senador Pompeu",
            "Senador Sá",
            "Sobral",
            "Solonópole",
            "Tabuleiro do Norte",
            "Tamboril",
            "Tarrafas",
            "Tauá",
            "Tejuçuoca",
            "Tianguá",
            "Trairi",
            "Tururu",
            "Ubajara",
            "Umari",
            "Umirim",
            "Uruburetama",
            "Uruoca",
            "Varjota",
            "Várzea Alegre",
            "Viçosa do Ceará"],
    "brasilia": ["Brasília"],
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

function validarRG() {
  const inputRg = document.getElementById("rg").value;
  const rgSemPontuacao = inputRg.replace(/\D/g, '');
  
  if (rgSemPontuacao.length !== 9) {
    alert("RG inválido. Deve conter exatamente 9 dígitos.");
    return;
  }

  const numeroRG = rgSemPontuacao.slice(0, 8);
  const digitoConf = rgSemPontuacao.slice(8);
  console.log(numeroRG)
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

const cpf        = document.getElementById('cpf')
let botao_alterar   = document.querySelector('.submit_btn')
let form_alterar    = document.getElementById('form_alterar')


const selectEstado = document.querySelector('select[name="estado"]');
const selectCidade = document.querySelector('select[name="cidade"]');

selectEstado.addEventListener('change', function() {
  const estadoSelecionado = this.value;
  
  // Limpa as opções do dropdown de cidades
  selectCidade.innerHTML = '<option selected disabled class="form_select_option" value="">Selecione</option>';
  
  // Verifica se um estado foi selecionado
  if (estadoSelecionado) {
    const cidades = cidadesPorEstado[estadoSelecionado];
    let city = document.getElementById('cidade').value
    // Adiciona as opções de cidades no dropdown correspondente
    cidades.forEach((cidade) => {
      const optionElement = document.createElement('option');
      optionElement.textContent = cidade;
      optionElement.value = cidade;
      selectCidade.appendChild(optionElement);
      if(city.value=cidade){
        optionElement.selected = true
      }
    });
  }
});

function removerPontuacaoRG(rg) {
  return rg.replace(/[^\d]/g, "");
}
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
    const cpf = document.getElementById('cpf')
    formataCPF(cpf);
    const rg  = document.getElementById('rg')
    formatarRG(rg)

    rg.addEventListener('input',()=>{
      formatarRG(rg)
    })

    cpf.addEventListener('input',()=>{
      formataCPF(cpf)
    })
 }

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

window.addEventListener("DOMContentLoaded", (event) => {
let dataNascimento = document.getElementById('dtnasc_func')
dataNascimento.addEventListener('input',()=>{
  formatarNascimento(dataNascimento)
})
});
function removerMascaraCPF(cpf) {
return String(cpf).replace(/\D/g, '');
}
botao_alterar.addEventListener('click',()=>{
  event.preventDefault();
  if(validaCpf(cpf.value)==true){
    if(validarRG()==true){
      cpf.value = removerMascaraCPF(cpf.value)
      rg.value  = removerPontuacaoRG(rg.value)
      form_alterar.submit()
    }else{
      console.log(validarRG())
      alert("RG Inválido!")
    }
   
  }else{
    alert("CPF Inválido!")
  }
  
})
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