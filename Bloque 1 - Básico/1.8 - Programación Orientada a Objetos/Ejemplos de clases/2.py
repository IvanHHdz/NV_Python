class Lista:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea, prioridad, estado='Pendiente'):
        self.tareas.append({
            'tarea': tarea,
            'prioridad': prioridad,
            'estado': estado
        })
    
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea['tarea']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}")
    
    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1]['estado'] = 'Completada'
            print(f"Tarea '{self.tareas[indice - 1]['tarea']}' marcada como completada.")
        else:
            print("Índice de tarea inválido.")
            
            
def main():
    mi_lista = Lista()
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            tarea = input("Ingrese la tarea: ")
            prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
            mi_lista.agregar_tarea(tarea, prioridad)
        elif opcion == '2':
            mi_lista.mostrar_tareas()
        elif opcion == '3':
            indice = int(input("Ingrese el índice de la tarea a completar: "))
            mi_lista.completar_tarea(indice)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    

if __name__ == "__main__":
    main()