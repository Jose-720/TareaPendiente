#EJERCICIO 4: Uso de super() en Herencia Múltiple

class Forma:
    def dibujar(self):
        print("Dibujando forma")

class Color:
    def __init__(self, color):
        self.color = color
    
    def pintar(self):
        print("Pintando con", self.color)

class CuadradoColorido(Forma, Color):
    def __init__(self, lado, color):
        super().__init__() 
        super().__init__(color)
        self.lado = lado

    def dibujar(self):
        super().dibujar()
        print("Dibujando un cuadrado de lado", self.lado)

# Crear una instancia de CuadradoColorido y llamar a los métodos
cuadrado = CuadradoColorido(5, "rojo")
cuadrado.dibujar()
cuadrado.pintar()
