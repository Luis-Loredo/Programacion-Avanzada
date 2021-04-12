class cuenta:
    (cliente, cuenta, saldo, deposito, retiro)
    self.cliente = cliente
    self.cuenta = cuenta
    self.saldo = saldo
    self.deposito = deposito
    self.retiro = retiro

    def setConsignar (self, s):
        self.saldo = self.saldo + s
    def setretiro (self, s):
        if (self.saldo - s > 0 ):
            self.saldo = self.saldo - s
    
    def getcuenta (self):
        return self.cuenta
    def getcliente (self):
        return self.cliente
    def getdeposito (self):
        return self.deposito
    def getsaldo (self):
        return self.saldo

    def mostrarcuenta(self):
        print("\ncuenta: " + self.getcuenta() + "\ncliente: " + self.getcliente() + "\ndeposito: " + str(self.getdeposito() + "\nsaldo: "+ str(self.saldo())))

cuenta = raw_input ("Favor de ingresar el numero de cuenta: ")
cliente = raw_input ("Favor de ingresar el numero de cliente: ")
saldo = input("Su saldo es: ")
retiro = input("Fondos insuficientes: ")
e = cuenta(cuenta, cliente, saldo)
e.mostrarcuenta