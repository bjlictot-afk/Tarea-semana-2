# ---------------------------------------------------------
# EJEMPLO DE ABSTRACCIÓN EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------

# La abstracción consiste en mostrar solo lo esencial
# y ocultar los detalles internos del funcionamiento.
# Para esto usamos clases abstractas y métodos abstractos.

from abc import ABC, abstractmethod

# ---------------------------------------------------------
# CLASE ABSTRACTA
# ---------------------------------------------------------
# Esta clase NO se puede crear como objeto.
# Solo sirve como molde para otras clases.
class Animal(ABC):

    # Método abstracto:
    # Las clases hijas están obligadas a implementarlo.
    @abstractmethod
    def hacer_sonido(self):
        pass


# ---------------------------------------------------------
# CLASE HIJA 1 (Perro)
# ---------------------------------------------------------
# Hereda de Animal y debe implementar el método hacer_sonido.
class Perro(Animal):

    def hacer_sonido(self):
        return "Guau"


# ---------------------------------------------------------
# CLASE HIJA 2 (Gato)
# ---------------------------------------------------------
class Gato(Animal):

    def hacer_sonido(self):
        return "Miau"


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
# Aquí se crean objetos de Perro y Gato.
# No se puede crear un objeto de Animal porque es abstracto.
if __name__ == "__main__":
    perro = Perro()
    gato = Gato()

    print("El perro hace:", perro.hacer_sonido())
    print("El gato hace:", gato.hacer_sonido())
