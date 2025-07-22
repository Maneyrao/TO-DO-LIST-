tareas = []
tareas_realizadas = []
tareas_pendientes = []

def agregar_tarea(inputt):
    if not inputt.strip():
        return("No podés agregar una tarea vacía.")
    for tarea in tareas_pendientes:
        if tarea["descripción"].lower() == inputt.lower().strip() and tarea["estado"] == "pendiente":
            print("Esa tarea ya está pendiente.")
            return

    nueva_tarea = {
        "descripción": inputt,
        "estado": "pendiente"
    }

    tareas_pendientes.append(nueva_tarea)
    print(f'Se agregó la tarea: "{inputt}"')
    
def recorrerlista():
    if not tareas_pendientes:
        return "no tenes tareas máquina\n"
    resultado= "estas son las tareas pendientes\n"
    for tarea in tareas_pendientes:
        resultado += f"{tarea}\n"
    return resultado

def eliminar_tarea(inputt, lista):
        for tarea in lista:
            if tarea["descripción"].lower().strip() == inputt:
                lista.remove(tarea)
                return f'Tarea eliminada: "{inputt}"'
        return "No se encontró esa tarea."
def marcas_tareas(inputt):
    for tarea in tareas_pendientes:
        if tarea["descripción"].lower().strip() == inputt:
                tareas_pendientes.remove(tarea)
                tareas_realizadas.append(tarea)
                return(f"Tarea marcada como hecha: {inputt}")
    else:
        return("No se encontró la tarea.")
def cerrar_programa():
    exit()
    return"Gracias por usar la lista de tareas"


