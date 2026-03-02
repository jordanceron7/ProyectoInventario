import json
from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}
        self.ids_registrados = set()

    def añadir_producto(self, producto: Producto):
        if producto.get_id() in self.ids_registrados:
            print("Error: El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto
        self.ids_registrados.add(producto.get_id())
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto: str):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.ids_registrados.remove(id_producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print("Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[id_producto].set_cantidad(cantidad)

        if precio is not None:
            self.productos[id_producto].set_precio(precio)

        print("Producto actualizado correctamente.")

    def buscar_por_nombre(self, nombre: str) -> list:
        resultados = [
            producto
            for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, archivo: str):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(
                {id_: prod.to_dict() for id_, prod in self.productos.items()},
                f,
                indent=4
            )

    def cargar_desde_archivo(self, archivo: str):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                for id_, prod_data in data.items():
                    producto = Producto.from_dict(prod_data)
                    self.productos[id_] = producto
                    self.ids_registrados.add(id_)
        except FileNotFoundError:
            pass