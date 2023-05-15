#crear una calculadora para operaciones aritmeticas
#y que contenga un menu. 
#Resolver con funciones por separado!

def Calculadora():
    
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    texto = (input("Que operacion desea realizar?: ")).title()
    if(texto == "Suma"):
        Suma(num1,num2)
    elif(texto == "Resta"):
        Resta(num1,num2)
    elif(texto == "Multiplicacion"):
        Multiplicacion(num1,num2)
    else:
        Divicion(num1,num2)
        
def Suma(num1,num2):
    resultado = num1 + num2
    print(resultado)

def Resta(num1,num2):
    if(num1 > num2):
        resultado = num1 - num2
        print(resultado)
    else:
        resultado = num2 - num1
        print(resultado)

def Multiplicacion(num1,num2):
    resultado = num1 * num2
    print(resultado)

def Divicion(num1,num2):
    resultado = num1 % num2
    print(resultado)

Calculadora()


