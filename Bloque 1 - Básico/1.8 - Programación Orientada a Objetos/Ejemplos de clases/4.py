class Lista:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea, prioridad, estado='Pendiente'):
        self.tareas.append({
            'tarea': tarea,
            'prioridad': prioridad,
            'estado': estado
        })
    
    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1]['estado'] = 'Completada'
            print(f"Tarea '{self.tareas[indice - 1]['tarea']}' marcada como completada.")
        else:
            print("Índice de tarea inválido.")
    
    def __len__(self):
        return len(self.tareas)
    
    def __str__(self):
        return "\n".join([f"{i + 1}. {tarea['tarea']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}" 
                            for i, tarea in enumerate(self.tareas)]) if self.tareas else "No hay tareas en la lista."

    def __getitem__(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea = self.tareas[indice]
            return f"{indice + 1}. {tarea['tarea']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}"
        else:
            raise IndexError("Índice de tarea inválido.")

    def __setitem__(self, indice, valor):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice] = valor
        else:
            raise IndexError("Índice de tarea inválido.")

def main():
    mi_lista = Lista()
    mi_lista.agregar_tarea("Comprar víveres", "Alta")
    mi_lista.agregar_tarea("Lavar el coche", "Media")
    
    print(f"Número de tareas en la lista: {len(mi_lista)}")
    
    print(mi_lista)
    
    print(mi_lista[0])
    
    cambiar_tarea = {
            'tarea': "Llevar el coche al taller",
            'prioridad': "Alta",
            'estado': "Pendiente"
        }

    mi_lista[1] = cambiar_tarea
    
    print("Después de cambiar la segunda tarea:")
    print(mi_lista)

if __name__ == "__main__":
    main()