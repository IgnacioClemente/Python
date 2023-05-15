#Escribir un programa que muestre todo lo que
#usuario introduzca hasta que le usuario escriba salir

def EscribirHasta():
    escribir = input("Escriba lo que quiera: ").title()
    while(escribir != "Salir"):
        print(escribir)
        escribir = input("Escriba lo que quiera: ").title()
EscribirHasta()
