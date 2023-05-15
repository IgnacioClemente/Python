class Animal():
    def __init__(self,tipo,comida,altura):
        self._tipo = tipo
        self._comida = comida
        self._altura = altura
    @property
    def tipo(self):
        return self._tipo
    @property
    def comida(self):
        return self._comida
    @property
    def altura(self):
        return self._altura
    @tipo.setter
    def tipo(self):
        self._tipo = self._tipo
    @comida.setter
    def comida(self):
        self._comida = self._comida
    @altura.setter
    def altura(self):
        self._altura = self._altura
    def __str__(self):
        return "\nTipo: {} \nComida: {} \nAltura: {}".format(self.tipo, self.comida,self.altura)