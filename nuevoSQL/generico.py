import mysql.connector
from mysql.connector import Error

class Generico():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost', 
                port = 3306, #el puerto del xampp
                user = 'root',
                password = '',
                database = '', #poner el nombre de la base de datos de mysql
            )
        except Error as ex:
            print('Error en la conexion con la base de datos: {0}'.format(ex))

    def listar(self):
       if self.conexion.is_connected(): #booleano
        try:
            cursor = self.conexion.cursor() #booleano
            cursor.execute("SELECT * FROM VUELOS") ##ejecuto un query
            respuesta = cursor.fetchall() ##trae todo lo que encuentra en la base de datos
            return respuesta
        except Error as ex:
            print('Error listar los registros de vuelos: {0}'.format(ex))

    def registrar(self,vuelo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #booleano
                sql = ("INSERT INTO VUELOS (nro, fecha, hora, ciudad, personal, patente) VALUES ({0}, '{1}', '{2}', '{3}', {4}, '{5}')")#agrego estos datos
                cursor.execute(sql.format(vuelo[0],vuelo[1],vuelo[2],vuelo[3],vuelo[4],vuelo[5]))#ejecuto 
                self.conexion.commit()#lo agrego
                print('Vuelo registrado')
            except Error as ex:
                print('Error listar los registros de vuelos: {0}'.format(ex))

    def actualizar(self,vuelo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #booleano
                actualizar = ("UPDATE VUELOS SET fecha = '{0}', hora = '{1}', ciudad = '{2}', personal = {3}, patente = '{4}' WHERE nro = {5}")#actualizo estos datos
                cursor.execute(actualizar.format(vuelo[1],vuelo[2],vuelo[3],vuelo[4],vuelo[5],vuelo[0]))#el 0 va al final porque es el numero a editar de metodos
                self.conexion.commit()#lo agrego
                print('Vuelo Actualizado')
            except Error as ex:
                print('No se pudo realizar la actualizacion: {0}'.format(ex))

    def eliminar(self,vueloEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #booleano
                eliminar = "DELETE FROM VUELOS WHERE nro = {0}"#ejecuto la consulta
                cursor.execute(eliminar.format(vueloEliminar))#ejecuto el eliminar
                self.conexion.commit()#lo elimino
                print('Vuelo Eliminado')
            except Error as ex:
                print('No se pudo eliminar el vuelo: {0}'.format(ex))
    
    def buscar(self,vueloBuscar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #booleano
                buscar = "SELECT * FROM VUELOS WHERE nro = {0}"
                cursor.execute(buscar.format(vueloBuscar))#ejecuto el eliminar
                print('Vuelo Encontrado')
                respuesta = cursor.fetchone() ##trae todo lo que encuentra en la base de datos
                print(respuesta)
                return respuesta
            except Error as ex:
                print('No se pudo encontrar el vuelo: {0}'.format(ex))
