from PersonasPoo import Persona
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad,matricula):
        super().__init__(nombre, apellido, edad)
        self.matricula = matricula
    def __str__(self):
        return super().__str__() +f'\nMatricula: {self.matricula}'
alumno = Alumno('Juan','Medina',25,1234)
print(alumno)