# -*- coding: utf-8 -*-
#######################################
##  LOCATE FAMILY Brazil 
##    Lista de brasileiros do Locate Family Brazil com nome, sobrenome, telefone, endereco
##
##    Author: Alex Benincasa Santos 
##    Mail: alexbenincasa@ymail.com
##    2019
#######################################

import json
import requests
from bs4 import BeautifulSoup

lista = []
lista_telefone = []

for page in xrange(1,12500):
	
	# Paginação
	result = requests.get('https://www.locatefamily.com/Street-Lists/Brazil/index-{}.html'.format(page))

	# BeautifulSoup faz o parser no result colocando as tags
	soup = BeautifulSoup(result.text, features='html.parser')

	for li in soup.select('ul.list-inline'):
		nome = li.find('span', {'itemprop': 'familyName'})
		sobrenome = li.find('span', {'itemprop': 'givenName'})
		telefone = li.find('li', {'itemprop': 'telephone'})
		endereco = li.find('li', {'itemprop': 'address'})

		if not nome or not sobrenome or not telefone or not endereco:
			continue

		telefone = telefone.text.encode('utf-8').strip()

		# se o telefone já existe não cadastra o registro
		if telefone in lista_telefone:
			continue

		lista_telefone.append(telefone)

		nome = nome.text.encode('utf-8').strip()
		sobrenome = sobrenome.text.encode('utf-8').strip()
		endereco = endereco.text.encode('utf-8').strip()

		lista.append({ 'nome': nome, 'sobrenome': sobrenome, 'telefone': telefone, 'endereco': endereco })

with open('locate-family-brazil.json', mode="w") as f:
	f.write(json.dumps(lista, indent=4))

