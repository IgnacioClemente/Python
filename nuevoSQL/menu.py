from generico import Generico
from metodos import Metodos

def menu():
    avanza = True
    while avanza:
        correcta = False
        while not correcta:
            print('1- Listar')
            print('2- Registrar')
            print('3- Actualizar')
            print('4- Eliminar')
            print('5- Buscar')
            opcion = int(input('Ingrese un opcion: '))
            if(opcion < 1 and opcion > 5):
                print('No valido')
            elif opcion == 5:
                avanza = False
            else:
                correcta = True
                opciones(opcion)


def opciones(opcion):
    gene = Generico()
    met = Metodos()
    if opcion == 1:
        try:
            vuelos = gene.listar()
            if len(vuelos) > 0:
                met.listar(vuelos)
            else:
                print('No se encontro registros')
        except:
            print('Ocurrio un error')
    elif opcion == 2:
        vuelos = met.registro()
        try:
            gene.registrar(vuelos)
        except:
            print('Error en el registro')
    elif opcion == 3:
        try:
            vuelo = gene.listar()# si hay registros
            if len(vuelo) > 0: # si encontro el registro
                vuelo = met.actualizar(vuelo)
                if vuelo: # si encontre el numero
                    gene.actualizar()
                else:
                    print('No se encontro el numero')
            else:
                print('No contiene registros')
        except:
            print('Error en el actualizado')
    elif opcion == 4:
        try:
            vuelo = gene.listar()
            if len(vuelo) > 0:
                vueloE = met.eliminar(vuelo)
                if not (vueloE == ""):# si no esta vacio
                    gene.eliminar(vueloE)
                else:
                    print('No se encontro el numero')
            else:
                print('Error al eliminar')
        except:
            print('No se pudo eliminar')
    elif opcion == 5:
        try:
            vuelo = gene.listar()
            if len(vuelo) > 0:
                vueloE = met.buscar(vuelo)
                if not (vueloE == ""):# si no esta vacio
                    gene.buscar(vueloE)
                    met.listar(vueloE)
                else:
                    print('No se encontro el numero')
            else:
                print('Error al buscar')
        except:
            print('No se pudo buscar')
menu()
