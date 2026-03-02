from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\nSISTEMA DE GESTIÓN DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Salir")


def main():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto: ")
            cantidad = input("Nueva cantidad (dejar vacío para no modificar): ")
            precio = input("Nuevo precio (dejar vacío para no modificar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for producto in resultados:
                print(producto)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
            print("Inventario guardado correctamente.")

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario.json")
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()