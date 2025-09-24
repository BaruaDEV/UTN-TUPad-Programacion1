# Parcial 1 de programacion

opcion_menu = [
    "1. Ingresar titulo (sin ejemplares)",
    "2. Ingresar ejemplares disponibles (sin titulo)",
    "3. Mostrar catálogo",
    "4. Consultar disponibilidad de un titulo en especifico",
    "5. Listar agotados",
    "6. Agregar Titulo (con ejemplares)",
    "7. Actualizar ejemplares (prestamos/devolucion)",
    "8. Ver catálogo completo",
    "9. Salir"
]

libros = ["El señor de los anillos", "Orgullo y prejuicio", "Matar un Ruiseñor"]
ejemplares = [5,3,7]

while True:
    print("::::Menu::::\n")
    for opcion in opcion_menu:
        print (opcion)
    seleccion = input("Seleccione una opcion: ").strip()
    print("-"*30)

    if seleccion == "1":
        titulo = input("Ingrese titulo: ")

        while titulo in libros or titulo == "":
            print("*"*10)
            print("Titulo repetido o en blanco. Intente nuevamente")
            titulo = input("Ingrese nuevmente: ")
            print("*"*10)
            
        print(f"Titulo ingresado: {titulo}")
        libros.append(titulo)
        posicion = libros.index(titulo)
        ejemplares.insert(posicion, 0)

    elif seleccion == "2":
        pass
    elif seleccion == "3":
        pass
    elif seleccion =="4":
        pass
    elif seleccion == "5":
        pass
    elif seleccion == "6":
        pass
    elif seleccion == "7":
        pass
    elif seleccion == "8":
        pass
    elif seleccion == "9":
        print("\nFinalizando programa...")
        break