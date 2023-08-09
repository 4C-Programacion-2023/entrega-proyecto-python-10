"""""
realizar si algo se elimina reducir precio
"""""


if Carrito == []:
    print("no hay nada disponible para pagar")
    continue
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

