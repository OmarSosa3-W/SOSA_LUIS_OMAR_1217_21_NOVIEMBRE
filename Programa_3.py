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
