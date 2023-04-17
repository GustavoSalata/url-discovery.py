#!/bin/usr/ python3

import requests 

url = input("Insira sua URL aqui: ")
wordlist = input("Insira o caminho da Wordlist aqui: ")

with open(wordlist, 'r') as f:
	for linha in f:
		word = linha.strip()
		teste = f"{url}/{word}"
		resposta = requests.get(teste)
		if resposta.status_code == 200:
			print(teste, resposta.status_code)
