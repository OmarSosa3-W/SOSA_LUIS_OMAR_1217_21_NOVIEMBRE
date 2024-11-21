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
