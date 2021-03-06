[![HitCount](http://hits.dwyl.com/learning-crawlers/locatefamily-brazil.svg)](http://hits.dwyl.com/learning-crawlers/locatefamily-brazil)

# LOCATE FAMILY Brazil

Extração de dados com Beautiful Soup para listar os brasileiros do Locate Family

## Instalação

```
pip install requests beautifulsoup4 
```

## Modo de usar

Procure o path do python instalado no Windows:

```
/mnt/c/Users/alexb/AppData/Local/Programs/Python/Python37-32/python.exe listar.py
```

## Resultado

**Header**

Nome, Sobrenome, Telefone, Endereco

**Dados**

```json
[
    {
        "endereco": "RUA VITORIO TAFARELLO, 681 -132 06192150 OSASCO -SP", 
        "sobrenome": "De Medeiros Bezerra", 
        "telefone": "551194708", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA 4 Q 15 CASA 20 72870058 VALPARAISO DE GOIAS -GOIAS", 
        "sobrenome": "De Oliveira Pinheiro", 
        "telefone": "556136292970", 
        "nome": "Delton"
    }, 
    {
        "endereco": "RUA DO ENGENHO 270 93890000 NOVA HARTZ -RIO GRANDE DO SUL", 
        "sobrenome": "Eliane", 
        "telefone": "555135652792", 
        "nome": "Henkel"
    }, 
    {
        "endereco": "RUA PROJETADA P 180 CASA 45480000 MUTUIPE -BA", 
        "sobrenome": "Francisco Dos Santos Junior", 
        "telefone": "557536352297", 
        "nome": "Junicio"
    }, 
    {
        "endereco": "RUA VITORIO TAFARELLO 681 132 06192150 OSASCO -SP", 
        "sobrenome": "De Medeiros Bezerra", 
        "telefone": "551178632742", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA BARAO DO AMAZONAS 268 CASA 93344250 NOVO HAMBURGO -RS", 
        "sobrenome": "Rafael", 
        "telefone": "555130663871", 
        "nome": "Hennemann"
    }, 
    {
        "endereco": "RUA JORGE LACERDA 798 85810220 CASCAVEL -PR", 
        "sobrenome": "De Bona", 
        "telefone": "554599002322", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA MAURO PEIXOTO GOMES 21 AP 201 36774015 CATAGUASES -MINAS GERAIS", 
        "sobrenome": "Alberto Oliveira Mello", 
        "telefone": "553200000000", 
        "nome": "Carlos"
    }, 
    {
        "endereco": "RUA RUBENS FERREIRA DA SILVA, 77 30880470 BELO HORIZONTE -MG", 
        "sobrenome": "Pinheiro De Almeida Junior", 
        "telefone": "553134738859", 
        "nome": "Delvaci"
    }, 
    {
        "endereco": "RUA FERRAZ 71 69918422 RIO BRANCO -AC", 
        "sobrenome": "De Moura Costa", 
        "telefone": "556899711585", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA JOSE DO PATROCINIO 904 90050002 PORTO ALEGRE -RIO GRANDE DO SUL", 
        "sobrenome": "Martins Doberstein Me", 
        "telefone": "551140039011", 
        "nome": "Dely"
    }, 
    {
        "endereco": "RUA JOAQUIM FERREIRA 124 AP 1308 T 2 05033080 SAO PAULO -SP", 
        "sobrenome": "De Olival Fernandes", 
        "telefone": "551136485053", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA CAMARE 40 FDS 21620170 RIO DE JANEIRO -RJ", 
        "sobrenome": "De Oliveira", 
        "telefone": "552194354454", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA DA GLORIA, 67 09181650 SANTO ANDRE -SP", 
        "sobrenome": "Alberto Pereira", 
        "telefone": "551144258660", 
        "nome": "Carlos"
    }, 
    {
        "endereco": "RUA DOMINGOS GIGLIO 451 02972010 SAO PAULO -SP", 
        "sobrenome": "De Queiroz", 
        "telefone": "551139769971", 
        "nome": "Marizilda"
    }, 
    {
        "endereco": "RUA CORONEL MANOEL MARTINS JUNIOR, 340 12242810 SAO JOSE DOS CAMPOS -SP", 
        "sobrenome": "Martins Ferreira Jr", 
        "telefone": "551239220176", 
        "nome": "Delzuite"
    }, 
    {
        "endereco": "RUA ANTONIO TURIBIO TEIXEIRA BRAGA 280 CASA 15 82320380 CURITIBA -PARANA", 
        "sobrenome": "Arendt Gerowski", 
        "telefone": "554130391632", 
        "nome": "Marjo"
    }, 
    {
        "endereco": "RUA QUITANDINHA 23 2 ANDAR 07056080 GUARULHOS -SAO PAULO", 
        "sobrenome": "Cristina Gomes Pereira Bento", 
        "telefone": "551123041568", 
        "nome": "Marjorie"
    }, 
    {
        "endereco": "RUA PROFESSOR IVO CORSEUIL, 408 -APTO 601 90690410 PORTO ALEGRE -RS", 
        "sobrenome": "De Carvalho Leal Moreira", 
        "telefone": "555133287267", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA CAVALCANTE DE LACERDA, 266 -FUNDOS 05591010 SAO PAULO -SP", 
        "sobrenome": "Alberto Pereira Marques", 
        "telefone": "551137261228", 
        "nome": "Carlos"
    }, 
    {
        "endereco": "AV AURELIO BRITO 317 64240000 PIRACURUCA -PI", 
        "sobrenome": "De Carvalho Machado", 
        "telefone": "558633432181", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA MANUEL ANTONIO LEITE 490 60545300 FORTALEZA -CE", 
        "sobrenome": "De Castro Araujo", 
        "telefone": "558588121008", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA FREGUESIA DE SAO ROMAO 129 08180150 SAO PAULO -SP", 
        "sobrenome": "De Freitas Barbosa", 
        "telefone": "551125858342", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA VISCONDE DE INHAUMA 553 APARTMENT 23 13560190 SAO CARLOS -SAO PAULO", 
        "sobrenome": "Alberto Perencin De Arruda Ribeir", 
        "telefone": "551634113688", 
        "nome": "Carlos"
    }, 
    {
        "endereco": "RUA SENADOR VITORINO FREIRES 568 65715000 LAGO DA PEDRA -MA", 
        "sobrenome": "De Paulo De Lima Vieira", 
        "telefone": "559936441943", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA PEDRO RACHID 243 12212100 SAO JOSE DOS CAMPOS -SAO PAULO", 
        "sobrenome": "Kelly", 
        "telefone": "551236450548", 
        "nome": "Turci"
    }, 
    {
        "endereco": "RUA DO RETIRO, 1617 -BLOCO 3 A. 13209201 JUNDIAI -SP", 
        "sobrenome": "De Pdua Elias De Almeida", 
        "telefone": "551148564478", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA ALEIXO GARCIA 703 84035630 PONTA GROSSA -PR", 
        "sobrenome": "Ricardo", 
        "telefone": "554231220127", 
        "nome": "Turesso"
    }, 
    {
        "endereco": "RUA ANTONIA FELICIA DO REIS, 91 -CASA 30750220 BELO HORIZONTE -MG", 
        "sobrenome": "Carlos Da Silva", 
        "telefone": "553125115458", 
        "nome": "Junio"
    }, 
    {
        "endereco": "AVENIDA CABO ADAO PEREIRA 419 02936010 SAO PAULO -SP", 
        "sobrenome": "Ferreira Da Silva", 
        "telefone": "551145080255", 
        "nome": "Marjorie"
    }, 
    {
        "endereco": "CONJUNTO CAJAZEIRAS VII 001 RUA C BLOCO 11 AP 001 41337325 SALVADOR -BAHIA", 
        "sobrenome": "De Azevedo", 
        "telefone": "557132190511", 
        "nome": "Turis"
    }, 
    {
        "endereco": "R GOMES PEREIRA, ALM, 72 22291170 RIO DE JANEIRO -RJ", 
        "sobrenome": "Michel De Fournier", 
        "telefone": "552125416687", 
        "nome": "Henri"
    }, 
    {
        "endereco": "AV EVARISTO DELFINO PINTO 603 06890000 SAO LOURENCO DA SERRA -SP", 
        "sobrenome": "Cesar Da Silvs Eduardo", 
        "telefone": "551146864130", 
        "nome": "Junio"
    }, 
    {
        "endereco": "RUA QUIRINO QUADROS 1327 38500000 MONTE CARMELO -MG", 
        "sobrenome": "Cesar Dos Reis", 
        "telefone": "553438428877", 
        "nome": "Junio"
    }, 
    {
        "endereco": "RUA DAS SERINGUEIRAS 345 APTO 62 04321070 SAO PAULO -SP", 
        "sobrenome": "Mayumi Motoyama", 
        "telefone": "551150118677", 
        "nome": "Marjorie"
    }, 
    {
        "endereco": "CONJUNTO PRIMAVERA II CASA 16 QUADRA 01 64006130 TERESINA -PI", 
        "sobrenome": "De Sousa Borges", 
        "telefone": "558631312800", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA DOUTOR LUIZ AYRES, 1968 -C SALA 2 03568000 SAO PAULO -SP", 
        "sobrenome": "De Sousa Brasil Junior", 
        "telefone": "551127411822", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA JOSE MARTINS DA SILVA 24 AP 101 58050440 JOAO PESSOA -PB", 
        "sobrenome": "De Lucena Morais Filho", 
        "telefone": "558332313490", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA VICTOR MEIRELLES, 475 89560000 VIDEIRA -SC", 
        "sobrenome": "Marcos", 
        "telefone": "554935331293", 
        "nome": "Demartini"
    }, 
    {
        "endereco": "RUA RLC 1 S N 74491055 GOIANIA -GOIAS", 
        "sobrenome": "De Melo Ferreira", 
        "telefone": "556235884889", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA DOUTOR NIKOLAS 75 AP 1 32230460 CONTAGEM -MG", 
        "sobrenome": "De Melo Lima", 
        "telefone": "553130536298", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA ANTONIO FELIX 93 57039460 MACEIO -AL", 
        "sobrenome": "Georgia", 
        "telefone": "558233551862", 
        "nome": "Demas"
    }, 
    {
        "endereco": "RUA RUI BARBOSA 200 CASA DA FRENTEPADARIA 79980000 MUNDO NOVO -MATO GROSSO DO SUL", 
        "sobrenome": "Denizete Da Silva", 
        "telefone": "556734743411", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "AVENIDA MARQUES DE OLINDA 200 404 50030000 RECIFE -PE", 
        "sobrenome": "De Moura Fontes", 
        "telefone": "558197692121", 
        "nome": "Fernando"
    }, 
    {
        "endereco": "RUA CORONEL ANTONIO MENDES CARNEIRO 624 CASA 62010160 SOBRAL -CE", 
        "sobrenome": "Dennis Pereira De Souza", 
        "telefone": "558897295913", 
        "nome": "Antonio"
    }, 
    {
        "endereco": "RUA COQUEIRO 77 31150210 BELO HORIZONTE -MG", 
        "sobrenome": "Fernandes Amaral", 
        "telefone": "553130242957", 
        "nome": "Junio"
    }, 
    {
        "endereco": "RUA BELARMINO FERREIRA 226 CS 2 24460240 SAO GONCALO -RJ", 
        "sobrenome": "De Santana Menezes", 
        "telefone": "552131193101", 
        "nome": "Savio"
    }, 
    {
        "endereco": "AVENIDA LUIS DE MATOS 99 26255510 NOVA IGUACU -RIO DE JANEIRO", 
        "sobrenome": "Delforge De Vasconcelos", 
        "telefone": "552135843544", 
        "nome": "Henriette"
    }, 
    {
        "endereco": "RUA PAISSANDU, 906 -SALA 206 99010100 PASSO FUNDO -RS", 
        "sobrenome": "De Souza Mendes", 
        "telefone": "555492112743", 
        "nome": "Savio"
    }, 
    {
        "endereco": "AVENIDA DAS CEREJEIRAS 431 SOBRADO 02124000 SAO PAULO -SP", 
        "sobrenome": "Alberto Proena Jaques", 
        "telefone": "551123657250", 
        "nome": "Carlos"
    }, 
    {
        "endereco": "PRACA DOS GODINHOS 270 38750000 PRESIDENTE OLEGARIO -MG", 
        "sobrenome": "Ferreira Marra", 
        "telefone": "553438112497", 
        "nome": "Junio"
    }, 
    {
        "endereco": "RUA 9 1628 CASA 38740000 PATROCINIO -MINAS GERAIS", 
        "sobrenome": "Gomes De Oliveira", 
        "telefone": "553438324864", 
        "nome": "Junio"
    }
]
```