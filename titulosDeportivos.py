import requests
from bs4 import BeautifulSoup

ole = requests.get("https://ole.com.ar")

ole_src = ole.content

soup = BeautifulSoup(ole_src, 'lxml')

titulos= []

for h2_tag in soup.find_all("h2"):
	a_tag = h2_tag.find('a')
	titulo = a_tag.attrs['title']
	titulos.append(titulo)

for titulo in titulos:
	print(titulo,'\n')
