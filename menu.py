"hacer que printe bien el carrito"
from main import Camisetasact, Camisetasret
"Bienvenido a Mazacamisetas"
Carrito=[]

"LISTA EQUIPOS RETRO"
ListaB=["Boca juniors CAMPEON mundial de clubes 2003","Despedida de Roman","Camiseta del Diego","Camiseta 1990"]
ListaR=["River CAMPEON libertadores 2018","River CAMPEON mundial de clubes 1986","Despedida de ponzio","Camiseta river Libertadores 2015"]
ListaA=["Camepona del mundo 2022","Campeona del mundo 1986","Campeon Copa America 2021","Camiseta mundial 1990"]
ListaRM=["Campeon Champions 2017","Campeon de champion 2021","Campeon mundial de clubes 2018","Campeon Champions 2002"]
ListaM=["Campeon Champion 2007","Campeon de mundial de clubes 2007","Camiseta 1998"]


Sumatodo=[]


while True:
    try:
        menu=int(input("Que desea hacer? \n 1.Comprar una camiseta \n 2.Ver carrito \n 3.Pagar \n 4.Salir \n  >>>>  "))
        if menu == 1:
            tipo = int(input("Que tipo de camiseta quiere? \n 1.Actuales \n 2.Retro  \n >>>>  "))
            if tipo == 1:
                print("estos son los talles disponbles")
                talles=("s","m","l","xl","xxl")
                for talle in talles:
                    print(talle)
                talle = str(input("Que talle quiere? "))
                equipo = str(input("Que equipo quiere? "))
                camisetaf = Camisetasact(talle, equipo, 35)
                print(camisetaf)
                Sumatodo.append(35)
                try:
                    Carrito.append(camisetaf)
                    print("se ha agregado correctamente a su carrito")
                except AttributeError or ValueError:
                    print("no se ha podido agregar correctamente,intente de nuevo")
                continue
            elif tipo == 2:
                print("Solo poseemos camisetas retro de los siguientes clubes \n Boca \n River  \n Argentina \n Real Madrid \n Milan  ")
                sino=input("Desea continuar? ")
                while True:
                    if sino == "si":

                        print("estos son los talles disponbles")
                        talles = ("s", "m", "l", "xl", "xxl")
                        for talle in talles:
                            print(talle)
                        talle = str(input("Que talle quiere?: "))
                        equipo = str(input("Elije el equipo de su camiseta "))
                        if equipo == "Boca":
                            temporada=input(f"De BOCA JUNIORS tenemos el siguiente stock {ListaB}")
                        if equipo == "River":
                            temporada=input(f"De BOCA JUNIORS tenemos el siguiente stock {ListaR}")
                        if equipo == "Milan":
                            temporada=input(f"De BOCA JUNIORS tenemos el siguiente stock {ListaM}")
                        if equipo == "Real Madrid":
                            temporada=input(f"De BOCA JUNIORS tenemos el siguiente stock {ListaRM}")
                        if equipo == "Argentina":
                            temporada=input(f"De BOCA JUNIORS tenemos el siguiente stock {ListaA}")
                        Camisetaf = Camisetasret(talle, equipo, temporada, 70)
                        print(Camisetaf)
                        Carrito.append(Camisetaf)
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
                res=input("Desea eliminar alguna camiseta del carrito? (ingrese solo el equipo) ")
                if res == "si":
                    res3=input("Que tipo de camiseta desea eliminar retro o actual")
                    res2=input("que camiseta desea eliminar? ")
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
                    print("Se ha pagado satifactoriamente")
                    Dinerof = Dinerot - Tpagar
                    print(F"DINERO == {Dinerof}")
                if pagarR == "no":
                    continue

        elif menu == 4:
            break
        else:
            print("ERROR,elija algunas de las opciones.")
            continue
    except ValueError:
        print("No se toma como valor las letras.")
L