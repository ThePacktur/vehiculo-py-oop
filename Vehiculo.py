class Vehiculo:
 #inicializador o constructor "funcion"
    def __init__(self,modelo:str,marca:str,anio:int,cc:float,n_ruedas:int):         #el primer parametro que este dentro de una clase tiene que ser un self
        self.__modelo = modelo          #self.parametro = seria para un paramatro publico
        self.__marca = marca
        self.__anio = anio          #self.__parametro = seria para un parametro privado
        self.__cc = cc
        self.__n_ruedas = n_ruedas     #atributos entero.
        #sel f es el objeto que se esta creando. (yo como objeto me estoy asignando a un modelo)
    def set_modelo(self,modelo:str):
        self.__modelo = modelo
    
    def get_modelo(self):
        return self.__modelo
    
    def set_marca(self,marca:str):
        self.__marca = marca

    def get_marca(self):
        return self.__marca


    def set_anio(self,anio:int):
        self.__anio = anio

    def get_anio(self):  
        return self.__anio
     
    def set_cc(self,cc:float):
        self.__cc = cc

    def get_cc(self):
        return self.__cc

    def set_n_ruedas(self,n_ruedas:int):
        self.__n_ruedas = n_ruedas

    def set_n_ruedas(self):
        return self.__n_ruedas    
    #get retorna atributos privados y los set asignan un  nuevo valor a un atributo que es privado
    #get todos los get retornan
    #funcion str permite generar "retornar" un string que sirve para devolver un objeto
    #str = imprimir todo los contenidos.

    def __str__(self):
        txt = f"Modelo: {self.__modelo}"
        txt = f"Marca: {self.__marca}"
        txt = f"anio: {self.__anio}"
        txt = f"cc: {self.__cc}"
        txt = f"n_ruedas: {self.__n_ruedas}"
        return txt