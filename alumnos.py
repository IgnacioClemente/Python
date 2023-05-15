#Tenemos 3 alumnos con notas de 3 materias. Necesitamos
#saber el promedio de cada materia y 
#luego su promedio general. Si el resultado
#es mayor a 90 = A, 80= B, 70=C 60 =D. Definan el 
#ejercicio en varias funciones para su mejor desarrollo.

alumnosList=[]
notasList=[]
promedioList=[]

def Ingreso():
    for alumno in range(3):
        alumno = str(input("Escriba el nombre de un alumno: ")).title()
        alumnosList.append(alumno)
        
        for nota in range(3):
            nota = int(input("Escriba 3 notas para el primer alumno: "))
            notasList.append(nota)   
    Promedio()
        
def Promedio():
    prom1 = sum(notasList[0:3]) / 3
    promedioList.append(prom1)
    prom2 = sum(notasList[3:6]) / 3
    promedioList.append(prom2)
    prom3 = sum(notasList[6:]) / 3
    promedioList.append(prom3)
    promGeneral = sum(notasList) / len(notasList)
    
    if prom1 >= 90:
        print("El promedio del primer alumno es A")
    elif prom1 >= 80 and prom < 90:
        print("El promedio del primer alumno es B")
    elif prom1 >= 70 and prom <  80:
        print("El promedio del primer alumno es C")
    elif prom >= 60 and prom < 70:
        print("El promedio del primer alumno es D")

Ingreso()
