from Ingreso import Ingreso
from usuarios import Usuario
class Menu():
    def menu(self):
        ingresoObj = Ingreso()
        while True:
            print('''1- Registar, 2- Listar, 3- Modificar -4 Historial -5 EditarUsuario -6 BuscarUsuario -7 Eliminar Usuario''')
            opcion = int(input('Opcion: '))
            if opcion >= 1 and opcion <= 7:
                if opcion == 1:
                    ingresoObj.agregar()
                elif opcion == 2:
                    ingresoObj.mostrar()
                elif opcion == 3:
                    ingresoObj.editarSaldo()
                elif opcion == 4:
                    ingresoObj.historial()
                elif opcion == 5:
                    ingresoObj.editarUsuario()
                elif opcion == 6:
                    ingresoObj.buscar()
                elif opcion == 7:
                    ingresoObj.eliminar()
            else:
                print('Opcion Incorrecta')
                exit()
principal = Menu()
principal.menu()