from ingreso import Ingreso
class Menu():
    def menu(self):
        ingresoObj = Ingreso()
        while True:
            print('''1- Registar, 2- Listar, 3- EditarAuto -4 Historial -5 Buscar Auto -6 Eliminar Auto -7 Reparaciones -8 Salir''')
            opcion = int(input('Opcion: '))
            if opcion >= 1 and opcion <= 8:
                if opcion == 1:
                    ingresoObj.agregar()
                if opcion == 2:
                    ingresoObj.mostrar()
                if opcion == 3:
                    ingresoObj.editarAuto()
                if opcion == 4:
                    ingresoObj.historial()
                if opcion == 5:
                    ingresoObj.buscar()
                if opcion == 6:
                    ingresoObj.eliminar()
                if opcion == 7:
                    ingresoObj.reparaciones()
                if opcion == 8:
                    exit()
            else:
                print('Opcion Incorrecta')
                exit()
principal = Menu()
principal.menu()