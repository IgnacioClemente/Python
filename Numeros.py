##Ingresar por teclado 2 numeros
##monstrar suma, promedio

def Numeros():
    num1 = int (input("Ingrese un numero: "))
    num2 = int (input("Ingrese otro numero: "))
    suma = num1 + num2
    prom = suma / 2
    print("La suma es:", suma, "y el promedio:" ,prom)
Numeros()
