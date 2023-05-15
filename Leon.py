from Animales import Animal
class Leon(Animal):
    def __init__(self, tipo, comida, altura,id):
        super().__init__(tipo, comida, altura)
        self.id = id
    def __str__(self):
        return super().__str__() +f'\nId: {self.id}'
leon = Leon('Carnivoro','Ciervo',5,75644)
print(leon)