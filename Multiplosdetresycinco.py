def Multiplode():
    contador = 0
    acumulador = 0
    for x in range(1,50):
        if(x % 3 == 0 and x % 5 == 0):
            contador += 1
            acumulador += x
            print(x)
    print("Se encontraron", contador, "numeros")
    print("La suma de los numeros es", acumulador)
    print("El porcentaje es de", acumulador / contador)
        
Multiplode()
