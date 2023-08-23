from tkinter import*
import tkinter as tk
from tkinter import filedialog

window= Tk()
window.title("MILAN RETRO")
window.geometry("670x220")
window.configure(bg="white")

image = tk.PhotoImage(file='./imagenes/2007 M.png')
lb5 = tk.Label(window, image=image)
lb5.place(x=0,y=0)



image2 = tk.PhotoImage(file='./imagenes/Pirlo.png')
lb5 = tk.Label(window, image=image2)
lb5.place(x=250,y=0)

image3 = tk.PhotoImage(file='./imagenes/1998 (milan).png')
lb2 = tk.Label(window, image=image3)
lb2.place(x=450,y=-3)



window.mainloop()