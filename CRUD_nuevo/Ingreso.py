from usuarios import Usuario
listaUsuario = []
class Ingreso():
    def agregar(self):
        print('Registro')
        nombreCorrecto = False
        while not nombreCorrecto:
            nombre = str(input('Nombre: '))
            if len(nombre) >= 2 and len(nombre) <= 8:
                if nombre.istitle():
                    if nombre.isalpha():
                        nombreCorrecto = True
                    else:
                        print('El nombre no puede contener numeros')
                else:
                    print('El nombre debe tener una mayuscula')
            else:
                print('El nombre debe tener mas de un letra y menos de ocho')
        apellidoCorrecto = False
        while not apellidoCorrecto:
            apellido = str(input('Apellido: '))
            if len(apellido) >= 2 and len(apellido) <= 8:
                if apellido.istitle():
                    if apellido.isalpha():
                        apellidoCorrecto = True
                    else:
                        print('El apellido no puede contener numeros')
                else:
                    print('El apellido debe tener una mayuscula')
            else:
                print('El apellido debe tener mas de un letra y menos de ocho')
        dniCorrecto = False
        while not dniCorrecto:
            dni = (input('Dni: '))
            if len(dni) == 8 and dni.isnumeric():
                dniCorrecto = True
            else:
                print('El dni tiene que ser numeros y contener mas de 8 caracteres')
        deposito = int(input('Deposito: '))
        retiro = int(input('Retiro: '))
        usuarioObj = Usuario(nombre,apellido,dni,deposito,retiro)
        listaUsuario.append(usuarioObj)

    def mostrar(self):
        print('Los usuarios son: ')
        for usuario in listaUsuario:
            usuario.imprimir()
    
    def editarSaldo(self):
        print('Editar Saldo')
        dni = input('Ingrese el Dni: ')
        for usuario in listaUsuario:
            if dni == usuario.dni:
                deposito = int(input('Deposito: '))
                retiro = int(input('Retiro: '))
                usuario.editarSaldo(deposito,retiro)
                mod = usuario.modificaciones(deposito,retiro)
                usuario.historial.append(mod)
            else:
                print('No se encuentra el usuario')

    def editarUsuario(self):
        print('Editar Datos')
        dni = input('Ingrese el Dni: ')
        for usuario in listaUsuario:
            if dni == usuario.dni:
                nombreCorrecto = False
            while not nombreCorrecto:
                nombre = str(input('Nombre: '))
                if len(nombre) >= 2 and len(nombre) <= 8:
                    if nombre.istitle():
                        if nombre.isalpha():
                            nombreCorrecto = True
                        else:
                            print('El nombre no puede contener numeros')
                    else:
                        print('El nombre debe tener una mayuscula')
                else:
                    print('El nombre debe tener mas de un letra y menos de ocho')
            apellidoCorrecto = False
            while not apellidoCorrecto:
                apellido = str(input('Apellido: '))
                if len(apellido) >= 2 and len(apellido) <= 8:
                    if apellido.istitle():
                        if apellido.isalpha():
                            apellidoCorrecto = True
                        else:
                            print('El apellido no puede contener numeros')
                    else:
                        print('El apellido debe tener una mayuscula')
            else:
                print('El apellido debe tener mas de un letra y menos de ocho')
                deposito = int(input('Deposito: '))
                retiro = int(input('Retiro: '))
                usuario.editarUsuario(nombre,apellido,deposito,retiro)
                mod = usuario.modificaciones(deposito,retiro)
                usuario.historial.append(mod)
        else:
            print('No se encuentra el usuario')

    def historial(self):
        print('Historial')
        dni = input('Ingrese el Dni: ')
        for usuario in listaUsuario:
            if dni == usuario.dni:
                for mensaje in usuario.historial:
                    print(f'Modificaciones: {mensaje}')
            else:
                print('Historial no encontrado')

    def buscar(self):
        print('Buscar Usuario')
        dni = input('Ingrese el Dni: ')
        for usuario in listaUsuario:
            if dni == usuario.dni:
                usuario.imprimir()
            else:
                print('Usuario no encontrado')
    
    def eliminar(self):
        print('Eliminar Usuario')
        dni = input('Ingrese el Dni: ')
        for usuario in listaUsuario:
            if dni == usuario.dni:
                listaUsuario.remove(usuario)
                print('Usuario Eliminado')
            else:
                print('No se encuentra el usuario')