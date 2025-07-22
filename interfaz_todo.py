import time
from Lógica_todolist import (
    agregar_tarea,
    recorrerlista,
    eliminar_tarea,
    marcas_tareas,
    tareas_pendientes,
    tareas_realizadas,
    tareas
    cerrar_programa
)




def consultar_menu():
    menu_principal = (f"opción 1, añadir tarea", "opción 2, ver tareas", "opción 3, marcar como hecho", "opción 4, eliminar tarea", "opción 5, salir")
    elegí=("A ver, qué hacemos  ")
    for i in menu_principal:
            print(i)
    if elegí == "1":
            agregar_tarea()   
    elif elegí == "2":
            pendientes_o_realizadas()
    elif elegí == "3":
            marcas_tareas()
    elif elegí == "4":
            eliminar_tarea()
    elif elegí == "5":
            cerrar_programa()
    else:
        print ("Opción no válida")



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
                agregar_tarea()
            else:
                consultar_menu()    

    def tareas_pendientes_inexistentes():
        while True:   
            print("No hay tareas pendientes, queres agregar una? y/n")
            elegir2= input("y/n: ").lower().strip()
            if elegir2== "y":
                agregar_tarea()
            elif elegir2== "n": 
                consultar_menu()
            else:
                print("elegí una opción válida que no codeo al pedo")
    def pendientes_o_realizadas():
            if agregar_tarea== "p":
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

