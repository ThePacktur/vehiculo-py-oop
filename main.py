from Auto import Auto

auto1 = Auto("v16", "Nissan", 2000, 1.2)

auto2 = Auto("Tercel","Toyota",1993,1.4)

marca = input("Ingrese marca: ")
modelo = input("Ingrese modelo: ")
anio = int(input("Ingrese anio: "))
cc = float(input("ingrese cc: "))
auto3 = Auto(modelo,marca,anio,cc)

auto1.marca = "Hyundai"
#auto1.__anio = 2002 no utilizar si es privado.
#si hacer:
auto1.set_anio(2002)
print(f"Marca : {auto1.marca}")
print(f"Modelo: {auto1.modelo}")
print(f"Anio: {auto1.get_anio()}")
auto2.modelo = "susuki"
print(auto1)
print(auto2)
print(auto3)
