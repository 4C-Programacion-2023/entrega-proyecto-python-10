from main import Camisetasact, Camisetasret
from tkinter import*
import tkinter as tk
from tkinter import filedialog



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random



#verificación mail (email.mime)



print("Bienvenido a Mazacamisetas")
codigoo = random.randint(100000, 999999)
password = "khxqwlwstfmbxxcj"
me = "carreramatias1707@gmail.com"
you = input("Ingrese su email  >>> ")

email_boady = f"""
            <html><boady><p>Hola,gracias por registrarte.  \n Su codigo de verificacion es {codigoo}</p></boady></html> 
            """

message = MIMEMultipart("alternative", None, [MIMEText(email_boady, "html")])
message["subject"] = "CODIGO DE VERIFICACION "
message["from"] = me
message["to"] = you

#log in / sign up

try:
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(me, password)
    server.sendmail(me, you, message.as_string())
    server.quit()
    Verificacion = int(input("Ingrese el codigo de verificacion que le ha llegado "))
    while True:
        if Verificacion == codigoo:
            print("Se ha verificado correctamente")

            try:
                usuario = input("Ingrese su usuario ")
                contraseña = input("Ingrese su contraseña ")
                print("Se ha creado su usuario satifacoriamente ")
            except ValueError:
                print("No se ha podido crear su usuario, ingrese el usuario y contraseña sin numeros")
                break
            CarritoR = []
            CarritoA = []
            Carrito = []

            # listas de camisetas retro

            ListaB = ["Despedida Roman", "Camiseta Maradona", "Camiseta Boca Campeon 2002", "Camiseta Boca 2007"]
            ListaR = ["Despedida Ponzio", "Camiseta Campeon  2018", "Camiseta 1990"]
            ListaA = ["Campeona Mundial 1978", "Campeona Mundial 2022",  "Campeon Copa America 2021"]
            Listab = ["Camiseta de Cruyff", "Camiseta Campeon de champions 2015", "Camiseta Alternativa Azul"]
            ListaM = ["Camiseta Pirlo", "Camiseta de 1998", "Camiseta Campeon del mundial de clubes 2007 "]

            Sumatodo = []

            while True:
                try:
                    menu = int(
                        input(
                            "Que desea hacer? \n 1.Comprar una camiseta \n 2.Ver carrito \n 3.Pagar \n 4.Salir \n  >>>>  "))
                    if menu == 1:
                        tipo = int(input("Que tipo de camiseta quiere? \n 1.Actuales \n 2.Retro  \n >>>>  "))
                        if tipo == 1:

                            # compra camisetas actuales

                            print("estos son los talles disponbles")
                            talles = ("s", "m", "l", "xl", "xxl")
                            for talle in talles:
                                print(talle)
                            talle = str(input("Que talle quiere? "))
                            equipo = str(input("Que equipo quiere? "))
                            camisetaf = Camisetasact(talle, equipo, 35)
                            print(camisetaf)
                            Sumatodo.append(35)
                            CarritoA.append(camisetaf)
                            try:
                                Carrito.append(equipo)
                                print("se ha agregado correctamente a su carrito")
                            except AttributeError or ValueError:
                                print("no se ha podido agregar correctamente,intente de nuevo")
                            continue
                        elif tipo == 2:

                            # compra camisetas retro

                            print(
                                "Solo poseemos camisetas retro de los siguientes clubes \n Boca \n River \n Barcelona \n Argentina \n Milan  ")
                            sino = input("Desea continuar? (si o no) ")
                            sinoo=sino.lower()
                            while True:
                                if sinoo == "si":

                                    print("estos son los talles disponbles")
                                    talles = ("s", "m", "l", "xl", "xxl")
                                    for talle in talles:
                                        print(talle)
                                    talle = str(input("Que talle quiere?: "))
                                    equipo = str(input(
                                        "Elije el equipo de su camiseta \n 1.Boca \n 2.River \n 3.Barcelona \n 4.Argentina \n 5.Milan  "))
                                    if equipo == 1:
                                        window = Tk()
                                        window.title("BOCA JUNIORS RETRO")
                                        window.geometry("1800x400")
                                        window.configure(bg="white")
                                        image = tk.PhotoImage(file='./imagenes/2002.png')
                                        lb1 = tk.Label(window, image=image)
                                        lb1.place(x=-5, y=0)

                                        image2 = tk.PhotoImage(file='./imagenes/2007.png')
                                        lb5 = tk.Label(window, image=image2)
                                        lb5.place(x=345, y=0)

                                        image3 = tk.PhotoImage(file='./imagenes/maradona.png')
                                        lb2 = tk.Label(window, image=image3)
                                        lb2.place(x=575, y=-5)

                                        image4 = tk.PhotoImage(file='./imagenes/Droman.png')
                                        lb3 = tk.Label(window, image=image4)
                                        lb3.place(x=1000, y=0)

                                        window.mainloop()
                                        print(f"este es el stock que possemos{ListaB}")
                                        temporada = input("Ingrese la camiseta que desee: ")
                                    if equipo == 2:
                                        window = Tk()
                                        window.title("BOCA JUNIORS RETRO")
                                        window.geometry("1800x400")

                                        window.configure(bg="grey")

                                        image2 = tk.PhotoImage(file='./imagenes/ponzio.png')
                                        lb5 = tk.Label(window, image=image2)
                                        lb5.place(x=0, y=0)

                                        image3 = tk.PhotoImage(file='./imagenes/2018.png')
                                        lb2 = tk.Label(window, image=image3)
                                        lb2.place(x=450, y=-5)

                                        image4 = tk.PhotoImage(file='./imagenes/1998.png')
                                        lb3 = tk.Label(window, image=image4)
                                        lb3.place(x=1000, y=0)

                                        window.mainloop()

                                        print(f"este es el stock que possemos{ListaR}")
                                        temporada = input("Ingrese la camiseta que desee")
                                    if equipo == 4:
                                        from tkinter import *
                                        import tkinter as tk
                                        from tkinter import filedialog

                                        window = Tk()
                                        window.title("ARGENTINA RETRO")
                                        window.geometry("620x250")
                                        window.configure(bg="white")

                                        image = tk.PhotoImage(file='./imagenes/1978.png')
                                        lb5 = tk.Label(window, image=image)
                                        lb5.place(x=0, y=0)

                                        image2 = tk.PhotoImage(file='./imagenes/2021.png')
                                        lb5 = tk.Label(window, image=image2)
                                        lb5.place(x=230, y=0)

                                        image3 = tk.PhotoImage(file='./imagenes/2022.png')
                                        lb2 = tk.Label(window, image=image3)
                                        lb2.place(x=420, y=-3)

                                        window.mainloop()
                                        print(f"este es el stock que possemos{ListaA}")
                                        temporada = input("Ingrese la camiseta que desee")
                                    if equipo == 3:
                                        window = Tk()
                                        window.title("BARCELONA RETRO")
                                        window.geometry("1000x500")
                                        window.configure(bg="white")

                                        image = tk.PhotoImage(file='./imagenes/2015 (barca).png')
                                        lb5 = tk.Label(window, image=image)
                                        lb5.place(x=0, y=0)

                                        image2 = tk.PhotoImage(file='./imagenes/maradona (barca).png')
                                        lb5 = tk.Label(window, image=image2)
                                        lb5.place(x=500, y=0)

                                        image3 = tk.PhotoImage(file='./imagenes/Alternativa.png')
                                        lb2 = tk.Label(window, image=image3)
                                        lb2.place(x=700, y=-3)

                                        window.mainloop()
                                        print(f"este es el stock que possemos{Listab}")
                                        temporada = input("Ingrese la camiseta que desee")
                                    if equipo == 5:
                                        window = Tk()
                                        window.title("MILAN RETRO")
                                        window.geometry("670x220")
                                        window.configure(bg="white")

                                        image = tk.PhotoImage(file='./imagenes/2007 M.png')
                                        lb5 = tk.Label(window, image=image)
                                        lb5.place(x=0, y=0)

                                        image2 = tk.PhotoImage(file='./imagenes/Pirlo.png')
                                        lb5 = tk.Label(window, image=image2)
                                        lb5.place(x=250, y=0)

                                        image3 = tk.PhotoImage(file='./imagenes/1998 (milan).png')
                                        lb2 = tk.Label(window, image=image3)
                                        lb2.place(x=450, y=-3)

                                        print(f"este es el stock que possemos{ListaM}")
                                        temporada = input("Ingrese la camiseta que desee")
                                        window.mainloop()
                                    Camisetaf = Camisetasret(talle, equipo, temporada, 70)
                                    print(Camisetaf)
                                    CarritoR.append(Camisetaf)
                                    Carrito.append(equipo)
                                    Sumatodo.append(70)
                                    break
                                elif sinoo == "no":
                                    break
                                else:
                                    print("No se reconoce esa respuesta ingrese si o no")
                                    break
                            continue
                    elif menu == 2:

                        # ver carrito

                        if Carrito == []:
                            print("El Carrito está vacío \n   \n    \n   ")
                        else:
                            print(f"Su carrito es el siguiente: {Carrito}")
                            res = input("Desea eliminar alguna camiseta del carrito?  ")
                            if res == "si":
                                res3 = int(input("Que tipo de camiseta desea eliminar \n 1.retro \n 2.actual"))

                                if res3 == 1:
                                    print(CarritoR)
                                    res2 = input("que camiseta desea eliminar? (solo el equipo) ")
                                    Carrito.remove(res2)
                                    Sumatodo.remove(70)
                                elif res3 == 2:
                                    print(CarritoA)
                                    res2 = input("que camiseta desea eliminar? (solo el equipo) ")
                                    Carrito.remove(res2)
                                    Sumatodo.remove(35)


                            elif res == "no":
                                continue

                    elif menu == 3:

                        # pagar

                        if Carrito == []:
                            print("no hay nada disponible para pagar")
                            continue
                        if Carrito != []:
                            Dinero = 0
                            print("DINERO == 0")
                            Tpagar = sum(Sumatodo)
                            print(f"La suma total de lo que tiene que pagar: {Tpagar}")
                            Ingrese = int(input("ingrese la cantidad de dinero para pagar"))
                            Dinerot = Dinero + Ingrese
                            print("DINERO ACTUALIZADO")
                            print(f"DINERO == {Dinerot}")
                            pagarR = input("Desea pagar \n  1.si \n 2.no? ")

                            if pagarR == 1:
                                while True:

                                    # agregar dinero a la billetera

                                    if Dinerot == Tpagar:
                                        Dinerof = Dinerot - Tpagar
                                        print("Se ha pagado satifactoriamente")
                                        print(F"DINERO == {Dinerof}")
                                    elif Dinerot >= Tpagar:
                                        Dinerof = Dinerot - Tpagar
                                        print("Se ha pagado satifactoriamente")
                                        print(F"DINERO == {Dinerof}")

                                    elif Dinerot <= Tpagar:
                                        print("no se puede pagar, No hay suficiente dinero")
                                        llegar = input("Desea agregar dinero \n 1.si \n 2.no")
                                        if llegar == 1:
                                            Ingrese = int(input("ingrese la cantidad de dinero para pagar"))
                                            Dinerot = Dinero + Ingrese
                                            if Dinerot == Tpagar:
                                                Dinerof = Dinerot - Tpagar
                                                print("Se ha pagado satifactoriamente")
                                                print(F"DINERO == {Dinerof}")
                                            elif Dinerot >= Tpagar:
                                                Dinerof = Dinerot - Tpagar
                                                print("Se ha pagado satifactoriamente")
                                                print(F"DINERO == {Dinerof}")

                                            break
                                        elif llegar == 2:
                                            break

                            if pagarR == 2:
                                continue

                    elif menu == 4:
                        break
                    else:
                        print("ERROR,elija algunas de las opciones.")
                        continue
                except ValueError:
                    print("No se toma como valor las letras.")
        elif Verificacion != codigoo:
            print("No es correcto el codigo")
            break



except Exception as e:
    print(f"Error al enviar el email:{e}")










