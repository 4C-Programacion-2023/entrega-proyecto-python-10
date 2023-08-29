"bienvenido a MAZACAMISETAS"


class Camisetasact:
    def __init__(self,talle:str,equipo:str,precio:int):
        self.precio = precio
        self.talle = talle
        self.equipo = equipo
    def __str__(self):
        return f"talle: {self.talle}, equipo: {self.equipo}.Su precio es de {self.precio}usd"
class Camisetasret:
    def __init__(self, talle: str, equipo: str, precio:int):
        self.precio = precio
        self.talle = talle
        self.equipo = equipo



    def __str__(self):
        return f"CAMISETA RETRO \n talle: {self.talle}, equipo: {self.equipo},.Su precio es de {self.precio}usd"


