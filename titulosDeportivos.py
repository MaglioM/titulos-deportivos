import requests
import tkinter as tk
from bs4 import BeautifulSoup

def capturaTitulos(pagina):
	fuente = BeautifulSoup(requests.get(pagina).content, 'lxml')
	titulos = []
	for h2_tag in fuente.find_all("h2"):
		a_tag = h2_tag.find('a')
		titulo = a_tag.attrs['title']
		titulos.append(titulo)
	return titulos

def imprimeTitulos(fuente):
	titulos = ""
	for titulo in capturaTitulos(fuente):
		titulos += "\n" + titulo + "\n"
	return titulos

def main():
	ventana = tk.Tk()
	contenido = tk.Label(
		text = imprimeTitulos("https://ole.com.ar"),
		foreground = "white",
		background = "black")
	contenido.pack()
	ventana.mainloop()

main()
