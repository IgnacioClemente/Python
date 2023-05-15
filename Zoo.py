class Zoologico():
    def __init__(self,tiendas,acuarios,areas,precio):
        self.tiendas = tiendas
        self.acuarios = acuarios
        self._areas = areas
        self._precio = precio
    @property
    def areas(self):
        return self._areas
    @property
    def precio(self):
        return self._precio
    @areas.setter
    def areas(self,value):
        self._precio = value
    @precio.setter
    def precio(self,value):
        self._precio = value
    def __str__(self):
        return "\nTiendas: {} \nAcuarios: {} \nAreas: {} \nPrecio: {}".format(self.tiendas, self.acuarios,self.areas,self.precio)