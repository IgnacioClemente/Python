class Vehiculos():
    def __init__(self,ruedas,color,marca,puertas):
        self.ruedas = ruedas
        self.color = color
        self.marca = marca
        self.puertas = puertas
    #def __str__(self):#forma 1
         #return "\nMarca: {} \ncolor: {} \nPuertas: {}".format(self.marca, self.color,self.puertas)
    #def __str__(self):#forma 2
        #cadena = "Marca: " + self.marca + "Color: " + self.color
        #return cadena
    def __str__(self):#forma 3 #la f me permite imprimir los valores dentro de las {} sin usar el .format
        return f"""
        Marca: {self.marca},
        Color: {self.color},
        Puertas: {self.puertas}"""
    
    #def __str__(self):#forma 4
            #return f'''
        #Marca: {self.marca}, 
        #Color: {self.color},
        #Puertas: {self.puertas}'''

    def CajaManual(self):
        print("No es automatica y el color es:", auto.color)

auto = Vehiculos(4, "Rojo","Fiat", 4)
auto1 = Vehiculos(5,"Azul","Toyota",5)
print(auto)
print(auto1)

class Coche(Vehiculos):
    def __init__(self, ruedas, color, marca, puertas,techo):
        super().__init__(ruedas, color, marca, puertas)
        self.techo = techo
    def __str__(self):
        return super().__str__() + "\nTecho: {}".format(self.techo)
    
coche = Coche(5,"Azul","VW",5,"Desmontable")
coche1 = Coche(4,"Rojo","Suran",4,"Abierto")
print(coche)
print(coche1)
class Motos():
    pass
