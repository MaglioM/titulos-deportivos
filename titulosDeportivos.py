import requests
from bs4 import BeautifulSoup

ole = requests.get("https://ole.com.ar")

ole_src = ole.content

soupOle = BeautifulSoup(ole_src,'lxml')

titulos = []

def capturaTitulos(pagina):
	fuente = BeautifulSoup(requests.get(pagina).content, 'lxml')
	titulos = []
	for h2_tag in fuente.find_all("h2"):
		a_tag = h2_tag.find('a')
		titulo = a_tag.attrs['title']
		titulos.append(titulo)
	return titulos

def imprimeTitulos(fuente):
	for titulo in capturaTitulos(fuente):
		print(titulo,'\n')


imprimeTitulos("https://ole.com.ar")
