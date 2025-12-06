# ---------------------------------------------------------
# EJEMPLO DE POLIMORFISMO EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------

# El polimorfismo permite que diferentes clases
# tengan un método con el MISMO nombre,
# pero que cada una lo implemente de manera distinta.

class Animal:

    # Método que será "polimórfico"
    def hacer_sonido(self):
        pass


# ---------------------------------------------------------
# CLASE HIJA 1
# ---------------------------------------------------------
class Perro(Animal):

    def hacer_sonido(self):
        return "Guau"


# ---------------------------------------------------------
# CLASE HIJA 2
# ---------------------------------------------------------
class Gato(Animal):

    def hacer_sonido(self):
        return "Miau"


# ---------------------------------------------------------
# CLASE HIJA 3
# ---------------------------------------------------------
class Vaca(Animal):

    def hacer_sonido(self):
        return "Muuu"


# ---------------------------------------------------------
# FUNCIÓN QUE DEMUESTRA POLIMORFISMO
# ---------------------------------------------------------
def hacer_gritar(animal):
    # Aquí no importa si es Perro, Gato o Vaca
    # Siempre llama al mismo método:
    return animal.hacer_sonido()


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":

    animales = [Perro(), Gato(), Vaca()]

    for animal in animales:
        print("El animal hace:", hacer_gritar(animal))
