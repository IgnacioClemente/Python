class Metodos():
    
    def listar(self, vuelos):
        cantidad = 1
        for vuelo in vuelos:
            res = '{0}-- Numero: {1}, Fecha: {2}, Hora: {3}, Ciudad: {4}, Personal: {5}, Patente: {6}'
            print(res.format(cantidad, vuelo[0], vuelo[1],vuelo[2], vuelo[3], vuelo[4], vuelo[5]))
            cantidad += 1

    def registro(self):
        Numero = input('Numero: ')
        Fecha = input('Fecha: ')
        Hora = input('Numero: ')
        Ciudad = input('Ciudad: ')
        Personal = input('Personal: ')
        Patente = input('Patente: ')
        vuelo = (Numero,Fecha,Hora,Ciudad,Personal,Patente)
        return vuelo
    
    def actualizar(self,vuelo):
        numeroEditar = int(input('Numero a editar: '))
        numeroCorrecto = False
        for vue in vuelo:
            if vue[0] == numeroEditar:
                numeroCorrecto = True
                break
            if numeroCorrecto:
                Fecha = input('Fecha: ')
                Hora = input('Numero: ')
                Ciudad = input('Ciudad: ')
                Personal = input('Personal: ')
                Patente = str(input('Patente: '))
                vue = (numeroEditar,Fecha,Hora,Ciudad,Personal,Patente)
            else:
                vue = None
            return vue
        
    def eliminar(self,vueloEliminar):
        numeroCorrecto = False
        numeroEliminar = int(input('Numero a eliminar: '))
        for vue in vueloEliminar:
            if vue[0] == numeroEliminar:
                numeroCorrecto = True
                break
        if not numeroCorrecto:
            numeroEliminar = ""
        return numeroEliminar
    
    def buscar(self,vueloBuscar):
        numeroCorrecto = False
        numeroBuscar = int(input('Numero a buscar: '))
        for vue in vueloBuscar:
            if vue[0] == vueloBuscar:
                numeroCorrecto = True
                break
        if not numeroCorrecto:
            numeroBuscar = ""
        return numeroBuscar
        



