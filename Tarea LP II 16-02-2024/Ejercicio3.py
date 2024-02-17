#EJERCICIO 3: Polimorfismo con Clase Animal

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Creando objetos o instancias
Perro1 = Perro()
Gato1 = Gato()

# Llamando al método hacer_sonido
animales = [Perro1, Gato1]
for animal in animales:
    print(animal.hacer_sonido())
