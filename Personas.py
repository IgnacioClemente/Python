from Zoo import Zoologico
class Personas(Zoologico):
    def __init__(self, tiendas, acuarios, areas, precio,cantidad,edad):
        super().__init__(tiendas, acuarios, areas, precio)
        self._cantidad = cantidad
        self._edad = edad
    @property
    def cantidad(self):
        return self._cantidad
    @property
    def edad(self):
        return self._edad
    @cantidad.setter
    def cantidad(self,value):
        self._cantidad = value
    @edad.setter
    def edad(self,value):
        self._edad = value
    def __str__(self):
        return super().__str__()+f'\nCantidad: {self.cantidad} \nEdad: {self.edad}'