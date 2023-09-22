from Vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, modelo: str, marca: str, anio: int, cc: float,alfoja:int):
        super().__init__(modelo, marca, anio, cc, 2)
        self.__alfoja = alfoja
        
        #inlcuiir fet y set de alforja dado que son atributos de la moto.
    def __str__(self):
        txt = super().__str__()
        txt += f"\nAlfoja: {self.__alfoja}"
        return txt
