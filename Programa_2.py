class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self._titular = titular  # Variable que guarda el titular de la cuenta
        self._cantidad = cantidad  # Variable que guarda el saldo de la cuenta

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        print("No se puede modificar la cantidad directamente. Usa los métodos ingresar o retirar.")

    def mostrar(self):
        print(f"Titular: {self._titular}")  
        print(f"Cantidad: {self._cantidad}")  

    def ingresar(self, cantidad):
        if cantidad > 0:  
            self._cantidad += cantidad 
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0: 
            if cantidad <= self._cantidad: 
                self._cantidad -= cantidad
            else:
                print("No hay suficiente saldo para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

cuenta = Cuenta("Luis Omar Sosa", 1500.0) 
cuenta.mostrar() 

cuenta.ingresar(500)
cuenta.mostrar()

cuenta.retirar(200)
cuenta.mostrar()  

cuenta.retirar(2000)
cuenta.mostrar() 
