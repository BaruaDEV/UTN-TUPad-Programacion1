# Parcial 2do programacion
# Alumno: Barua, Mauro
import csv
import os

NOMBRE_ARCHIVO="productos.csv"

def obtener_productos():
    """Funcion para obtener los productos desde un archivo CSV o crear el Archivo csv con OS"""
    productos=[]
    # Si el archivo csv no existe, lo creamos utilizando OS con el metodo "w"
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            escritor.writeheader()
            return productos
        
    # Si el archivo ya existe lo abrimos
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector=csv.DictReader(archivo)

    # Agregamos a la lista productos los items del archivo csv, el precio lo convertimos a float
        for fila in lector:
            productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    return productos


def mostrar_productos():
    """ Funcion para mostrar todos los productos"""

    print("\n:::: Lista de Productos ::::\n")
    productos= obtener_productos()
    #iteramos sobre la lista de productos e imprimimos cada uno con su precio
    for i in productos:
        print(f'{i["nombre"]} - ${i["precio"]}')

def existe_producto(nombre):
    """ Funcion para comprobar si un producto ya existe"""

    productos=obtener_productos()
    # iteramos y comparamos si el producto ingresado esta en la lista
    for i in productos:
        if i["nombre"].lower() == nombre.strip().lower():
            return True
    return False

def validar_numero(precio):
    """ Funcion para validar el numero del producto ingresado"""
    # si posee mas de un punto '.' y no es un digito retornamos False
    if precio.count(".") > 1:
        return False
    if not precio.replace(".", "").isdigit():
        return False
    
    return True

def agregarLibro(libro):
    """ Funcion para agregar un nuevo producto"""

    # Agregamos con el metodo "a"
    with open(NOMBRE_ARCHIVO,"a", newline="", encoding="utf-8") as archivo:
        escritor= csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writerow(libro)

def agregar_producto():
    """ Funcion para solicitar nombre y precio de producto nuevo"""

    print("\n:::: Agregar nuevo Libro ::::\n")
    nombre = input("Ingrese nombre del titulo: ").strip()

    if existe_producto(nombre):
        print("El libro ya existe")
        return
    
    precio = input("Ingrese el precio: ").strip()

    if not validar_numero(precio):
        print("EL precio no es valido")
        return
    
    precio=float(precio)

    agregarLibro({"nombre": nombre, "precio": precio})

    print("\n¡El libro se agrego correctamente!")

def guardarProductos(libro):
    """ Funcion para guardar las modificaciones de un producto"""

    # usamos el modo 'w' para sobreescribir el archivo csv
    with open(NOMBRE_ARCHIVO,"w", newline="", encoding="utf-8") as archivo:
        escritor= csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(libro)

def editar_producto():
    """ Funcion para modificar un producto por el usuario"""

    nombre = input("Ingrese libro a modificar: ").strip()

    if not nombre:
        print("El nombre no puede ser vacio")
        return
    
    productos = obtener_productos()

    for i in productos:
        if i ["nombre"].lower() == nombre.lower():
            print("lalalala")
            precio = input("Ingrese nuevo precio: ").strip()

            if not validar_numero(precio):
                print("El precio no es valido")
                return
            
            i["precio"] = float(precio)

            guardarProductos(productos)
            print("¡El libro se ha actualizado correctamente!")
            break
    else:
        print("\nNo se encuentro el libro en el archivo")

def eliminar_producto():
    """ Funcion para eliminar un producto por un usuario"""

    nombre = input("\nIngrese libro a Eliminar: ").strip()

    if not nombre:
        print("El nombre no puede ser vacio")
        return
    
    productos = obtener_productos()
    productos_filtrados = []
    # Creamos una nueva listo sin el libro a eliminar
    for i in productos:
        if nombre.lower() != i["nombre"].lower():
            productos_filtrados.append(i)
    # Si la longuitud con cambia, no se elimina nada
    if len(productos_filtrados) == len(productos):
        print("EL producto no se encuentra en el archivo")
        return
    # Guardamos la nueva lista sin el producto eliminado
    guardarProductos(productos_filtrados)

    print("\nEl Libro fue eliminado correctamente")

def mostrar_menu():
    """ Funcion para iniciar el programa mostrando un menu y seleccionar accion"""

    while True:
        print(":"*30)
        print("1. Mostrar libro")
        print("2. Agregar libro")
        print("3. Editar precio de libro")
        print("4. Eliminar libro")
        print("5. Salir")
        print(":"*30)

        opcion= input("Ingrese opcion: ").strip()

        match opcion:
            case '1':
                mostrar_productos()
            case '2':
                agregar_producto()
            case '3':
                editar_producto()
            case '4':
                eliminar_producto()
            case '5':
                print("\nFinalizando programa...")
                break
            case _:
                print("\nOpción invalidá, ingrese un numero de 1 a 5")

# Inicia el programa
mostrar_menu()