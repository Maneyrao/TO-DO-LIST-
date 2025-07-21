import time

tareas_realizadas = []
tareas_pendientes = []
menu_principal = ["opción 1, añadir tarea", "opción 2, ver tareas", "opción 3, marcar como hecho", "opción 4, eliminar tarea", "opción 5, salir"]


def recorrerlista():
    print(f"estas son las tareas que quedan pendientes")    
    for tareas in tareas_pendientes:
        print(f"- {tareas}")

def continuar():
    continuar = input("¿Querés volver al menú? (y/n): ").lower().strip()
    if continuar == "y":
        print("dale, volvemos al menú")
        consultar_menu()
    else:
        print("bueno, te borro el system 32 porque no tengo paciencia")
        time.sleep(2)
        print("na mentira")
        time.sleep(1)
        print("volvemos al menú")
        consultar_menu()
        
        
def tareas_realizadas_inexistentes():
    print("no hiciste ninguna vago, mira toda las que te quedan pendientes")
    if tareas_pendientes:
        print("ah, tampoco tenes ganas de hacer mucho jajajaj hace algo vago")
        for tarea in tareas_pendientes:
            print(f"- {tarea}")
    else:
        print("no hay tareas pendientes, queres agregar una? y/n")
        elegir2= input("y/n: ").lower().strip()
        if elegir2== "y":
            opcion1()
        else:
            consultar_menu()

def tareas_pendientes_inexistentes():
    print("No hay tareas pendientes, queres agregar una? y/n")
    elegir2= input("y/n: ").lower().strip()
    if elegir2== "y":
        opcion1()
    elif elegir2== "n":
        continuar()
    else:
        print("elegí una opción válida que no codeo al pedo")
        tareas_pendientes_inexistentes()
def opcion1():
    while True:
        print("1. Añadimos tarea")
        tarea = input("Escribí la tarea: ").lower().strip()
        
        if not tarea.strip():
            print("No podés agregar una tarea vacía.")
            continue
        if tarea in tareas_pendientes:
            print("Esa tarea ya está pendiente.")
            continue
        
        tareas_pendientes.append(tarea)
        recorrerlista()
        print("agregamos otra? y/n")
        otratarea = input("y/n: ").lower()
        if otratarea != "y":
            break
    continuar()
            


def opcion2():
        elegir1= input("quieres ver las tareas pendientes o las realizadas? (p/r): ").lower()
        if elegir1== "p":
            if tareas_pendientes:
                recorrerlista()
            else:
                tareas_pendientes_inexistentes()
                continuar()
        elif elegir1== "r":
            if tareas_realizadas:
                recorrerlista()
            else:
                tareas_realizadas_inexistentes()
                continuar()
    
def opcion3():
    if tareas_pendientes:
        recorrerlista()
    else:
        tareas_pendientes_inexistentes()
        consultar_menu()
        
    tarea = input("Cuál realizaste? ").lower().strip()
    for t in tareas_pendientes:
        if t.lower() == tarea:
            tareas_pendientes.remove(t)
            tareas_realizadas.append(t)
            print(f"Tarea marcada como hecha: {t}")
            break
    else:
        print("No se encontró la tarea.")
def opcion4():
    while True:
        print("vas a eliminar una tarea? que vago que sos! mira, tenes estas para eliminar")
        if tareas_pendientes:
            recorrerlista()
            eliminar = input("cual vas a eliminar? ").lower().strip()
            if eliminar in tareas_pendientes:
                tareas_pendientes.remove(eliminar)
                print(f"Tarea eliminada: {eliminar}")
                eliminarotra = input("querés eliminar otra? y/n").lower().strip()
                if eliminarotra != "y":
                    consultar_menu()
                else:
                    continue
                
                time.sleep(1)
                if not tareas_pendientes:
                    print("ahora tenes no tenes tareas pendientes")
        else:
            tareas_pendientes_inexistentes()
            break
    eliminarotra = input("querés eliminar otra? y/n").lower().strip()
    if eliminarotra != "y":
        consultar_menu()        
def opcion5():
    print("Gracias por usar la lista de tareas")
    exit()
    


def consultar_menu():
    for i in menu_principal:
        print(i)
    elegí = input("elegí la opción: ").lower().strip()  
    if elegí == "1":
        opcion1()   
    elif elegí == "2":
        opcion2()
    elif elegí == "3":
        opcion3()
    elif elegí == "4":
        opcion4()
    elif elegí == "5":
        opcion5()
    else:
        print("Opción no válida")
        
consultar_menu()






