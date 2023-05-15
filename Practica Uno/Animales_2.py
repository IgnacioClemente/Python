from Zoo import Zoologico
class Animales_2(Zoologico):
    def __init__(self, tiendas, acuarios, areas, precio,tamaño,tipo):
        super().__init__(tiendas, acuarios, areas, precio)
        self._tamaño = tamaño
        self._tipo = tipo
    @property
    def tamaño(self):
        return self._tamaño
    @property
    def tipo(self):
        return self._tipo
    @tamaño.setter
    def tamaño(self,value):
        self._tamaño = value
    @tipo.setter
    def tipo(self,value):
        self._tipo = value
    def __str__(self):
        return super().__str__()+f'\nTamaño: {self.tamaño} \nTipo: {self.tipo}'