from Vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, modelo: str, marca: str, anio: int, cc: float):
        super().__init__(modelo, marca, anio, cc, 4)
