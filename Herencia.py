# ---------------------------------------------------------
# EJEMPLO DE HERENCIA EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------

# La herencia permite que una clase (hija) reutilice
# atributos y métodos de otra clase (padre).
# Esto evita repetir código y permite crear jerarquías.

# ---------------------------------------------------------
# CLASE PADRE
# ---------------------------------------------------------
class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        return f"{self.nombre} está comiendo."


# ---------------------------------------------------------
# CLASE HIJA 1 (Perro) que hereda de Animal
# ---------------------------------------------------------
class Perro(Animal):

    def ladrar(self):
        return f"{self.nombre} dice: Guau!"


# ---------------------------------------------------------
# CLASE HIJA 2 (Gato) que hereda de Animal
# ---------------------------------------------------------
class Gato(Animal):

    def maullar(self):
        return f"{self.nombre} dice: Miau!"


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":
    perro = Perro("Firulais")
    gato = Gato("Misu")

    print(perro.comer())      # método heredado de Animal
    print(perro.ladrar())     # método propio de Perro

    print(gato.comer())       # método heredado de Animal
    print(gato.maullar())     # método propio de Gato
