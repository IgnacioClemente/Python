#Ingresar por teclado una cantidad de numeros positivos y negativos
# y guardarlos en listas separadas. Positivos por un lado, y negativos por otro
#Extraer el numero de la lista de numeros Positivos
#que se encuentre en la posicion 1
#Remplazar uno de los numeros en la lista
#Remover cualquiera sin que sea la ultima de la lista

def ListasPosNeg():
    listaPos = []
    listaNeg = []
    for i in range(5):
        numeros = int (input("Escriba 5 numeros: "))
        if numeros < 0:
            listaNeg.append(numeros)
        else:
            listaPos.append(numeros)
    listaPos.pop(2)
    listaPos.insert(2, 7)
    listaNeg.sort(reverse=True)
    listaPos.sort(reverse=True) 
    print("Los numeros negativos son:", listaNeg)
    print("Los numeros postivos son:", listaPos)
    print("El primero numero de la lista de positivos es el:", listaPos[0])
ListasPosNeg()
