from auto import Auto
listaDeAutos = []
class Ingreso():
    def agregar(self):
        print('Registrar')
        patenteCorrecta = False
        while not patenteCorrecta:
            patente = str(input('Patente: '))
            if len(patente) >= 8 and len(patente) <= 16:
                if patente.isalnum():
                    patenteCorrecta = True
                else:
                    print('La patente debe tener mayusculas y numeros')
            else:
                print('La patente debe tener 8 caracteres')
        marcaCorrecta = False
        while not marcaCorrecta:
            marca = str(input('Marca: '))
            if len(marca) >= 2 and len(marca) <= 16:
                if marca.istitle():
                    if marca.isalpha():
                        marcaCorrecta = True
                    else:
                        print('La marca no puede contener numeros')
                else:
                    print('La marca debe tener una mayuscula')
            else:
                print('La marca debe tener mas de un letra')
        colorCorrecto = False
        while not colorCorrecto:
            color = str(input('Color: '))
            if len(color) >= 2 and len(color) <= 16:
                if color.istitle():
                    if color.isalpha():
                        colorCorrecto = True
                    else:
                        print('El color no puede contener numeros')
                else:
                    print('El color debe tener una mayuscula')
            else:
                print('El color debe tener mas de un letra')
        modeloCorrecto = False
        while not modeloCorrecto:
            modelo = str(input('Modelo: '))
            if len(modelo) >= 2 and len(modelo) <= 16:
                modeloCorrecto = True
            else:
                print('El modelo debe tener mas de un letra')
        autoObj = Auto(patente,marca,color,modelo)
        listaDeAutos.append(autoObj)
        
    def mostrar(self):
        print('Los autos son: ')
        for auto in listaDeAutos:
            auto.imprimir()
    
    def editarAuto(self):
        print('Editar Datos')
        patenteCorrecta = False
        patente = str(input('Ingrese la patente: '))
        for auto in listaDeAutos:
            if patente == auto.patente:
                patenteCorrecta = True
        if patenteCorrecta:
            marcaCorrecta = False
            while not marcaCorrecta:
                marca = str(input('Marca: '))
                if len(marca) >= 2 and len(marca) <= 16:
                    if marca.istitle():
                        if marca.isalpha():
                            marcaCorrecta = True
                        else:
                            print('La marca no puede contener numeros')
                    else:
                        print('La marca debe tener una mayuscula')
                else:
                    print('La marca debe tener mas de un letra')
            colorCorrecto = False
            while not colorCorrecto:
                color = str(input('Color: '))
                if len(color) >= 2 and len(color) <= 16:
                    if color.istitle():
                        if color.isalpha():
                            colorCorrecto = True
                        else:
                            print('El color no puede contener numeros')
                    else:
                        print('El color debe tener una mayuscula')
                else:
                    print('El color debe tener mas de un letra')
            modeloCorrecto = False
            while not modeloCorrecto:
                modelo = str(input('Modelo: '))
                if len(modelo) >= 2 and len(modelo) <= 16:
                    modeloCorrecto = True
                else:
                    print('El modelo debe tener mas de un letra')
            
            fecha = input('Fecha: ')
            arreglo = input('Arreglo: ')
            precio = input('Precio: ')
            auto.editarAuto(marca,color,modelo,fecha,arreglo,precio)
            mod = auto.modificaciones(fecha,arreglo,precio)
            auto.historial.append(mod)
        else:
            print('No se encuentra el Auto')

    def reparaciones(self):
        print('Reparaciones')
        patente = input('Ingrese la patente: ')
        for auto in listaDeAutos:
            if patente == auto.patente:
                fecha = input('Fecha: ')
                arreglo = input('Arreglo: ')
                precio = input('Precio: ')
                auto.reparaciones(fecha,arreglo,precio) 
                mod = auto.modificaciones(fecha,arreglo,precio)
                auto.historial.append(mod)
            else:
                print('No se encuentra el usuario')

    def historial(self):
        print('Historial')
        patente = input('Ingrese la patente: ')
        for auto in listaDeAutos:
            if patente == auto.patente:
                for mensaje in auto.historial:
                    print(f'Modificaciones: {mensaje}')
            else:
                print('Historial no encontrado')
                
    def buscar(self):
        print('Buscar Auto')
        patente = input('Ingrese la patente: ')
        for auto in listaDeAutos:
            if patente == auto.patente:
                auto.imprimir()
            else:
                print('Auto no encontrado')
    
    def eliminar(self):
        print('Eliminar Auto')
        patente = input('Ingrese la patente: ')
        for auto in listaDeAutos:
            if patente == auto.patente:
                listaDeAutos.remove(auto)
                print('Auto eliminado')
            else:
                print('No se encuentra el auto')