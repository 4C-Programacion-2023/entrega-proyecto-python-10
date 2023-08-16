"bienvenido a MAZACAMISETAS"


class Camisetasact:
    def __init__(self,talle:str,equipo:str,precio:int):
        self.precio = precio
        self.talle = talle
        self.equipo = equipo
    def __str__(self):
        return f"talle: {self.talle}, equipo: {self.equipo}.Su precio es de {self.precio}usd"
class Camisetasret:
    def __init__(self, talle: str, equipo: str, temporada:int,precio:int):
        self.precio= precio
        self.talle = talle
        self.equipo = equipo
        self.temporada=temporada



    def __str__(self):
        return f"talle: {self.talle}, equipo: {self.equipo},temporada: {self.temporada}.Su precio es de {self.precio}usd"






