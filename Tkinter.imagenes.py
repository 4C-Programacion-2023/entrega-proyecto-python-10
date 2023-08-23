from tkinter import*
import tkinter as tk

raiz=Tk()
raiz.title("Camiseta x")
raiz.resizable(False,False)
raiz.geometry("400x600")
raiz.config(bg="gray")

#creamos frame
miFrame=Frame()
miFrame.pack()

#agregamos el fondo con una imagen

miImagen=PhotoImage(file="imagenes.png")
raiz.mainloop()