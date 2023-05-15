class Vehiculos():
    def __init__(self,ruedas,color,marca,puertas):
        self.ruedas = ruedas
        self.color = color
        self.marca = marca
        self.puertas = puertas
    def CajaManual(self):
        print("No es automatica y el color es:", auto.color)

auto = Vehiculos(4, "Rojo","Fiat", 4)
auto.CajaManual()
auto1 = Vehiculos(5,"Azul","Toyota",5)
    
print("El color del auto es:", auto1.color, "Tiene", auto.ruedas, "Ruedas")
print("La marca del auto es:", auto.marca, "Tiene", auto.puertas, "Puertas")

class Coche(Vehiculos):
    def __init__(self, ruedas, color, marca, puertas,techo):
        super().__init__(ruedas, color, marca, puertas)
        self.techo = techo

    def ImprimeDatos(self):
        print("Los datos del coche: Ruedas", self.ruedas, "La cantidad de puetas es:", self.puertas, "Color", 
        self.color, "Marca", self.marca, "Puertas", self.puertas, self.techo, "Techo")

coche = Coche(5,"Azul","VW",5,"Desmontable")
coche1 = Coche(4,"Rojo","Sura",4,"Abierto")
coche.ImprimeDatos()
coche1.ImprimeDatos()

class Motos():
    pass
