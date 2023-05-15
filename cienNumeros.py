#Monstrar suma, promedio y la cantidad de los primeros 100 numeros
def cienNumeros():
    contador = 0
    acumulador = 0
    for i in range(100):
        contador +=1
        acumulador += i
    print("La cantidad es", contador)
    print("La suma de los numeros es", acumulador)
    print("El promedio es", acumulador / contador)
cienNumeros()
