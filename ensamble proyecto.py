from main import Camisetasact, Camisetasret



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


"Bienvenido a Mazacamisetas"
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

try:
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(me, password)
    server.sendmail(me, you, message.as_string())
    server.quit()
    Verificacion = int(input("Ingrese el codigo de verificacion que le ha llegado "))
    if Verificacion == codigoo:
        print("Se ha verificado correctamente")

        try:
            usuario = input("Ingrese su usuario ")
            contraseña = input("Ingrese su contraseña ")
            print("Se ha creado su usuario satifacoriamente ")
        except ValueError:
            print("No se ha podido crear su usuario, ingrese el usuario y contraseña sin numeros")


except Exception as e:
    print(f"Error al enviar el email:{e}")







Carrito=[]


Sumatodo=[]

while True:
    try:
        menu = int(
            input("Que desea hacer? \n 1.Comprar una camiseta \n 2.Ver carrito \n 3.Pagar \n 4.Salir \n  >>>>  "))
        if menu == 1:
            tipo = int(input("Que tipo de camiseta quiere? \n 1.Actuales \n 2.Retro  \n >>>>  "))
            if tipo == 1:
                print("estos son los talles disponbles")
                talles = ("s", "m", "l", "xl", "xxl")
                for talle in talles:
                    print(talle)
                talle = str(input("Que talle quiere? "))
                equipo = str(input("Que equipo quiere? "))
                camisetaf = Camisetasact(talle, equipo, 35)
                print(camisetaf)
                Sumatodo.append(35)
                try:
                    Carrito.append(equipo)
                    print("se ha agregado correctamente a su carrito")
                except AttributeError or ValueError:
                    print("no se ha podido agregar correctamente,intente de nuevo")
                continue
            elif tipo == 2:
                print(
                    "Solo poseemos camisetas retro de los siguientes clubes \n Boca \n River \n Independiente \n Barcelona \n Real Marid \n Milan \n Inter ")
                sino = input("Desea continuar? ")
                while True:
                    if sino == "si":

                        print("estos son los talles disponbles")
                        talles = ("s", "m", "l", "xl", "xxl")
                        for talle in talles:
                            print(talle)
                        talle = str(input("Que talle quiere?: "))
                        equipo = str(input("Elije el equipo de su camiseta "))
                        temporada = int(input("Ingrese el año "))
                        Camisetaf = Camisetasret(talle, equipo, temporada, 70)
                        print(Camisetaf)
                        Carrito.append(equipo)
                        Sumatodo.append(70)
                        break
                    elif sino == "no":
                        break
                    else:
                        print("No se reconoce esa respuesta ingrese si o no")
                        break
                continue
        elif menu == 2:
            if Carrito == []:
                print("El Carrito está vacío \n   \n    \n   ")
            else:
                print(f"Su carrito es el siguiente: {Carrito}")
                res = input("Desea eliminar alguna camiseta del carrito? (ingrese solo el equipo) ")
                if res == "si":
                    res3 = input("Que tipo de camiseta desea eliminar retro o actual")
                    res2 = input("que camiseta desea eliminar? ")
                    Carrito.remove(res2)
                    if res3 == "retro":
                        Sumatodo.remove(70)
                    elif res3 == "actual":
                        Sumatodo.remove(35)


                elif res == "no":
                    continue

        elif menu == 3:
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
                pagarR = input("Desea pagar?")

                if pagarR == "si":
                    while True:
                        print("Se ha pagado satifactoriamente")
                        if Dinerot == Tpagar:
                            Dinerof = Dinerot - Tpagar
                            print(F"DINERO == {Dinerof}")
                        elif Dinerot >= Tpagar:
                            Dinerof = Dinerot - Tpagar
                            print(F"DINERO == {Dinerof}")
                        elif Dinerot <= Tpagar:
                            print("no se puede pagar, No hay suficiente dinero")
                            llegar=input("Desea agregar dinero")
                            if llegar == "si":
                                Ingrese = int(input("ingrese la cantidad de dinero para pagar"))
                                Dinerot = Dinero + Ingrese
                                continue
                            elif llegar == "no":
                                break

                if pagarR == "no":
                    continue

        elif menu == 4:
            break
        else:
            print("ERROR,elija algunas de las opciones.")
            continue
    except ValueError:
        print("No se toma como valor las letras.")



if Carrito == []:
    print("no hay nada disponible para pagar")
if Carrito != []:
    Dinero=0
    print("DINERO == 0")
    Tpagar=sum(Sumatodo)
    print(f"La suma total de lo que tiene que pagar: {Tpagar}")
    Ingrese=int(input("ingrese la cantidad de dinero para pagar"))
    Dinerot=Dinero + Ingrese
    print("DINERO ACTUALIZADO")
    print(f"DINERO == {Dinerot}")
    pagarR=input("Desea pagar?")
    Sumatodo = 0
    if pagarR == "si":
        print("Se ha pagado satifactoriamente")
        Dinerof=Dinerot - Tpagar
        print(F"DINERO == {Dinerof}")
    if pagarR == "no":
        pass

