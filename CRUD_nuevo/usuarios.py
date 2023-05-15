class Usuario():
    def __init__(self,nombre,apellido,dni,deposito,retiro):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.deposito = deposito
        self.retiro = retiro
        self.saldo = (deposito - retiro)
        self.historial = []

    def imprimir(self):
        print('\nNombre: {} \nApellido: {} \nDNI: {} \nDeposito: {} \nRetiro: {}'.format(self.nombre, self.apellido,self.dni, self.deposito, self.retiro))
    
    def editarSaldo(self,deposito,retiro):
        self.deposito += deposito
        self.retiro += retiro
        self.saldo += (deposito-retiro)

    def editarUsuario(self,nombre,apellido,deposito,retiro):
        self.nombre = nombre
        self.apellido = apellido
        self.deposito = deposito
        self.retiro = retiro
        self.saldo = ( deposito-retiro)
    
    def modificaciones(self,deposito,retiro):
        return('\nDeposito: {} \nRetiro: {}'.format(deposito,retiro))

