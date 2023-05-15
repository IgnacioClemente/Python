class Auto():
    def __init__(self,patente,marca,color,modelo):
        self.patente = patente
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.historial = []

    def imprimir(self):
        print('\nPatente: {} \nMarca: {} \nColor: {} \nModelo: {}'.format(self.patente, self.marca,self.color, self.modelo))

    def editarAuto(self,marca,color,modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
    
    def modificaciones(self,fecha,arreglo,precio):
        return('\nFecha: {} \nArreglo: {} \nPrecio: {}'.format(fecha,arreglo,precio))
    
    def reparaciones(self,fecha,arreglo,precio):
        self.fecha = fecha
        self.arreglo = arreglo
        self.precio = precio