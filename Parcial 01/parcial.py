# Parcial 1 de programacion
# Alumno: Barua, Mauro

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

libros = ["El señor de los anillos", "Orgullo y prejuicio", "Matar un Ruiseñor"] # Libros iniciales a disposicion
ejemplares = [5,3,7] # ejemplares iniciales a disposicion

while True:
    print("\n::::Menu::::\n")
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
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para ingresar cantidad de ejemplares")
            continue
        for i, titulo in enumerate(libros):
            print(f"{i+1}. {titulo}")

        posicion = int(input("Ingrese el numero del titulo, para asignarle ejemplares: ")) -1

        while posicion < 0 or posicion >= (len(libros)):
            print("Posicion invalida, intente nuevamente")
            posicion = int(input("Ingrese el numero del titulo, para asignarle ejemplares: ")) -1
        
        cantidad = int(input("Ingrese cantidad de ejemplares del titulo: "))
        ejemplares[posicion] += cantidad
        print(f"Actualizacion: titulo: {libros[posicion]}, ejemplares disponibles: {ejemplares[posicion]}")

    elif seleccion == "3":
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para ingresar cantidad de ejemplares")
            continue
        print("\n:::::Catálogo de libros:::::\n")
        for i, titulo in enumerate(libros):
            print(f"{i+1}. {titulo}")

    elif seleccion =="4":
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para consultar")
            continue
        print("\n:::::libros Disonibles para consulta:::::\n")
        for i, titulo in enumerate(libros):
            print(f"{i+1}. {titulo}")

        posicion = int(input("Ingrese el numero del titulo, para consultar disponibilidad: ")) -1

        while posicion < 0 or posicion >= (len(libros)):
            print("Posicion invalida, intente nuevamente")
            posicion = int(input("Ingrese el numero del titulo, para asignarle ejemplares: ")) -1
        
        print(f"\nLa disponibilidad del libro: {libros[posicion]}, es de: {ejemplares[posicion]} ejemplares\n")

    elif seleccion == "5":
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para consultar")
        else:
            agotados = False
            print("\n::: Lista de titulos agotados:::\n")
        
            for i in range(len(libros)):
                if ejemplares[i] == 0:
                    print(libros[i])
                    agotados = True
                
        if not agotados:
             print("No hay libros agotados\n")
                    
    elif seleccion == "6":
        nuevo_libro = input("Ingrese un nuevo titulo/libro: ")
        if nuevo_libro in libros:
            print(f"El libro: {nuevo_libro}, ya esta registrado!")
        else:
            libros.append(nuevo_libro)
            posicion = libros.index(nuevo_libro)
            cantidad = int(input("Ingrese cantidad de ejemplares del libro ingresado: "))
            ejemplares.insert(posicion, cantidad)
            print(f"Titulo: {nuevo_libro}, agregado al catálogo con la cantidad de: {cantidad} ejemplares disponibles")
            
    elif seleccion == "7":
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para ingresar cantidad de ejemplares")
            continue

        for i, titulo in enumerate(libros):
            print(f"{i + 1}. {titulo}")
        
        posicion = int(input("Ingrese numero del libro para prestamo o devolucion: ")) -1

        while posicion < 0 or posicion >= (len(libros)):
            print("Posicion invalida, intente nuevamente")
            posicion = int(input("Ingrese el numero del titulo: ")) -1

        accion = input("Ingrese 'p' para prestamo o 'd' para devolucion: ").lower()

        if accion == "p":
            if ejemplares[posicion] > 0:
                ejemplares[posicion] -= 1
                print(f"Prestamo realizado. Ejemplares disponibles de: {libros[posicion]}: {ejemplares[posicion]}")
            else:
                print(f"No hay ejemplares disponibles para {libros[posicion]}")

        elif accion == "d":
            cantidad_devolucion = int(input("Ingrese la cantidad a devolver: "))
            if cantidad_devolucion < 0:
                print("Error, la devolucion minima es de 1")
            else:
                ejemplares[posicion] += cantidad_devolucion
                print("Devolucion realizada")
        else:
            print("Accion invalida. Use 'p' (prestamo) o 'd' (devolucion)")

    elif seleccion == "8":
        if not libros:
            print("No hay libros disponibles. Deben exisitir libros disponibles para ingresar cantidad de ejemplares")
            continue
        print(":::: CATALOGO COMPLETO ::::\n")
        for i, titulo in enumerate(libros):
            print(f"{i + 1}. {titulo}, ejemplares disopnibles: {ejemplares[i]}")

    elif seleccion == "9":
        print("\nFinalizando programa...")
        break