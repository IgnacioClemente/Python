##Ingresar por teclado 5 numeros
##monstrar suma, promedio

def Numeros():
    contador = 0
    suma = 0
    for i in range(5):
        num = int(input("Ingrese un numero: "))
        contador +=1
        suma += num
    prom = suma / contador
    print(contador)
    print("La suma es:",suma, "Y el promedio:",prom)
Numeros()

#con while
#contador = 0
#while contador < 6:
    #contado += 1
    #numero = int(input("Ingrese un numero"))
    #suma += numero
#promedio = suma / contador
#print(suma)
#print(promedio)
