from os import system

class Lista:
    def __init__(self):
        self.tareas = []
    
    def agregar(self, cantidad, nombre, precio_estimado, precio_real=None):
        self.tareas.append({
            'cantidad': cantidad,
            'nombre': nombre,
            'precio_estimado': precio_estimado,
            'precio_real': precio_real,
            'estado': False if precio_real is None else True
        })
        
    def __str__(self):
        encabezado = (
            "Lista de compras:\n"
            + "- " 
            + "cantidad nombre".ljust(30) + "| "
            + "precio estimado".ljust(15) + "| "
            + "precio real".ljust(13) + "| "
            + "Estado".ljust(13) + "|\n"
            + "-"*75 + "\n"
        )

        filas = ""
        for tarea in self.tareas:
            fila = (
                "- " +
                f"{tarea['cantidad']} {tarea['nombre']}".ljust(30) + "| " +
                f"L. {tarea['precio_estimado']}".ljust(15) + "| " +
                f"{f"L. {tarea['precio_real']}" if tarea['precio_real'] is not None else '~~~'}".ljust(13) + "| " +
                f"{'no comprado' if tarea['estado'] is False else 'listo'}".ljust(13) + "|\n"
            )
            filas += fila
        total_estimado = sum(
            tarea['precio_estimado'] for tarea in self.tareas if tarea['precio_estimado'] is not None
        )
        total_gastado = sum(
            tarea['precio_real'] for tarea in self.tareas if tarea['precio_real'] is not None
        )
        estimado_por_gastar = 0
        for tarea in self.tareas:
            if tarea['precio_real'] is None:
                estimado_por_gastar += tarea['precio_estimado'] if tarea['precio_estimado'] is not None else 0

        return encabezado + filas + "-"*75 + f"\nTotal estimado: L. {total_estimado}\nTotal gastado: L. {total_gastado}\nEstimado por gastar: L. {estimado_por_gastar}"

    def __len__(self):
        return len(self.tareas)

    def __getitem__(self, index):
        return self.tareas[index]

mi_lista = Lista()
ejecucion = True

def main():
    opciones = {        
        "1": agregar,
        "2": mostrar,
        "3": completar,
        "4": salir
    }
    
    while ejecucion:
        system('cls')
        print("Opciones:")
        print("[1] - Agregar producto")
        print("[2] - Mostrar lista")
        print("[3] - Completar")
        print("[4] - Salir")
        opcion = input("Seleccione una opción: ")

        try:
            opciones[opcion]()
        except KeyError:
            input("Opción no válida\nIntente de nuevo\n")
        except ValueError:
            input("Verifique los datos ingresados\n")

def agregar():
    nombre = input("Ingrese el nombre del producto: ")
    if len(nombre) > 24:
        nombre = nombre[:21] + "..."
    cantidad = int(input("Ingrese la cantidad: "))
    precio_estimado = float(input("Ingrese el precio estimado: "))
    mi_lista.agregar(cantidad, nombre, precio_estimado)

def mostrar():
    print(mi_lista)
    input("Presione enter")
    
def completar():
    index = int(input("Ingrese el índice del producto comprado: ")) - 1
    if index >= len(mi_lista):
        input("Verifique los datos ingresados\n")
        return
    elif mi_lista[index]["estado"]:
        input("Verifique los datos ingresados\nEse producto ya se compró antes\n")
        return
    precio = float(input(f"Ingrese el valor por el que se compró {mi_lista[index]['nombre']}: "))
    mi_lista[index]['estado'] = True
    mi_lista[index]['precio_real'] = precio
    
def salir():
    global ejecucion
    ejecucion = False

if __name__ == "__main__":
    main()