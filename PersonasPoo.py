class Persona():
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self):
        self.__nombre = self.__nombre

    def __str__(self):
        return "\nNombre: {} \nApellido: {} \nEdad: {}".format(self.nombre, self.apellido,self.edad)