#ADMINISTRADOR DE TAREAS
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class AdministradorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Índice de tarea fuera de rango")

    def mostrar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"{i + 1}. {tarea.descripcion} - {estado}")
        else:
            print("No hay tareas")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
        else:
            print("Índice de tarea fuera de rango")

# Ejemplo de uso
if __name__ == "__main__":
    administrador = AdministradorTareas()
    
    while True:
        print("\n--- ADMINISTRADOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            administrador.agregar_tarea(descripcion)
        elif opcion == "2":
            administrador.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            administrador.eliminar_tarea(indice)
        elif opcion == "3":
            administrador.mostrar_tareas()
        elif opcion == "4":
            administrador.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea completada: ")) - 1
            administrador.marcar_completada(indice)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
