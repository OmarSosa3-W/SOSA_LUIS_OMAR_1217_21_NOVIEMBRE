# SOSA_LUIS_OMAR_1217_21_NOVIEMBRE
Practicas del 21 de  noviembre 
# PROGRAMA 1:
# Clase Persona
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        # Inicializa los datos de la persona: nombre, edad y DNI
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        # Devuelve los datos de la persona como texto
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        # Verifica si la persona tiene 18 años o más
        return self.edad >= 18


if __name__ == "__main__":
    persona = Persona("Luis Omar Sosa", 18, "157694238")
    print(persona.mostrar())
    print("Mayor de edad:", persona.esMayorDeEdad())

![image](https://github.com/user-attachments/assets/cc39c8fb-63a2-48e5-b11e-44daceff1774)
![image](https://github.com/user-attachments/assets/27260fa8-79fa-41db-a94a-660410059d1a)

# PROGRAMA 2:
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

![image](https://github.com/user-attachments/assets/02a798af-241e-4efa-838f-bc1e5b5b3aa5)
![image](https://github.com/user-attachments/assets/961c3077-932a-4ded-af96-9fb4b13ed2f1)

# PROGRAMA 3:
# Clase Persona
class Persona:
    def __init__(self, nombre, edad, dni):
        # Inicializamos los atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):

        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return f"Cuenta - Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}"

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):

        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def mostrar(self):
        # Muestra los detalles de la cuenta joven, incluyendo la bonificación
        return f"Cuenta Joven - Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%"

# Aquí comienza el programa
if __name__ == "__main__":
    # Crear una persona (titular)
    persona = Persona("Luis Omar Sosa", 20, "12345678A")

    # Crear una cuenta joven con bonificación
    cuenta_joven = CuentaJoven(persona, 1000, 5)

    # Mostrar los detalles de la cuenta joven
    print(cuenta_joven.mostrar())

![image](https://github.com/user-attachments/assets/15b24231-816b-4697-a585-60b1ad87ee45)
![image](https://github.com/user-attachments/assets/eb6eece6-43b1-4c5e-881e-29acb7c1dda4)
