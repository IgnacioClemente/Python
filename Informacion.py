from Animales_2 import Animales_2
from Personas import Personas
elephante = Animales_2(5,4,12,540,7,'Carnivoro')
oso = Animales_2(6,15,45,8,320,'Omnivoro')
juan = Personas(8,4,3,450,3,40)
esteban = Personas(2,10,35,900,35,60)
print(elephante)
elephante.tamaño = 40
elephante.tipo = 'Hervivoro'
juan.edad = 25
juan.cantidad = 8
print('\nAnimales: ')
print('\nElephante: ')
print(elephante)
print('\nOso: ')
print(oso)
print('\nPersona: ')
print('\nJuan: ')
print(juan)
print('\nEsteban: ')
print(esteban)