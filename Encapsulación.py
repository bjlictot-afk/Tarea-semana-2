# ---------------------------------------------------------
# EJEMPLO DE ENCAPSULACIÓN EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------

# La encapsulación consiste en proteger los datos internos
# de una clase para que no se puedan modificar directamente.
# Para esto usamos atributos privados (__atributo)
# y métodos getters y setters para acceder a ellos.

class Persona:

    # Constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad       # atributo privado

    # Getter para nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para edad
    def get_edad(self):
        return self.__edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":
    persona = Persona("Belgica", 18)

    print("Nombre inicial:", persona.get_nombre())
    print("Edad inicial:", persona.get_edad())

    # Cambiando valores usando setters
    persona.set_nombre("Belgica J.")
    persona.set_edad(19)

    print("\nNombre actualizado:", persona.get_nombre())
    print("Edad actualizada:", persona.get_edad())
