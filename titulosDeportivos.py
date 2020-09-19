import requests
from tkinter import *
import tkinter.font as font
from bs4 import BeautifulSoup
from listaExcluidos import excluidos

def capturaTitulos(pagina,target):
	fuente = BeautifulSoup(requests.get(pagina).content, 'lxml')
	titulos = []
	for tag in fuente.find_all(target):
		for titulo in tag.findAll(text=True):
			titulo = titulo.replace('\n','')
			titulos.append(titulo)
	return titulos


def imprimeTitulos(master,pagina,target):
	for child in master.winfo_children():
		child.destroy()
	contenido = Text(master,
			foreground="#ffa",
			background="#025")
	for titulo in capturaTitulos(pagina,target):
		if titulo not in excluidos:
			contenido.insert(END,titulo+'\n\n')
	contenido.pack()
	scrollbar = Scrollbar(master)
	scrollbar.config(command=contenido.yview)
	scrollbar.pack(side=RIGHT, fill=Y)


def main():
	ventana = Tk()
	ancho = 600
	alto = 600
	canvas = Canvas(ventana,height=alto,width=ancho,bg="#000525")
	canvas.pack()
	#Cuadros
	botonera = Frame(canvas, bg='#025')
	botonera.place(relx=0.5,rely=0.01,relwidth=0.9,relheight=0.2,anchor='n')
	cuadroTitulos = Frame(canvas, bg='#025')
	cuadroTitulos.place(relx=0.5,rely=0.22,relwidth=0.9,relheight=0.6,anchor='n')
	#Botones
	fuenteBoton = font.Font(size=40,family='Palatino Linotype',weight='bold')
	Ole = Button(botonera,
		text="Olé",
		bg='#136',
		fg='#ffa',
		activebackground='#025',
		activeforeground='#ffa',
		font=fuenteBoton,
		command=lambda:imprimeTitulos(cuadroTitulos,"https://ole.com.ar",'h2'))
	Ole.place(relx=0.15,rely=0.05,relwidth=0.3,relheight=0.9,anchor='n')
	ESPN = Button(botonera,
		text="ESPN",
		bg='#136',
		fg='#ffa',
		activebackground='#025',
		activeforeground='#ffa',
		font=fuenteBoton,
		command=lambda:imprimeTitulos(cuadroTitulos,"https://espn.com.ar",'h1'))
	ESPN.place(relx=0.5,rely=0.05,relwidth=0.3,relheight=0.9,anchor='n')
	TyC = Button(botonera,
		text="TyC",
		bg='#136',
		fg='#ffa',
		activebackground='#025',
		activeforeground='#ffa',
		font=fuenteBoton,
		command=lambda:imprimeTitulos(cuadroTitulos,"https://tycsports.com",'h2'))
	TyC.place(relx=0.85,rely=0.05,relwidth=0.3,relheight=0.9,anchor='n')
	ventana.mainloop()


main()
