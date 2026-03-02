class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Métodos setters
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def set_precio(self, precio: float):
        if precio >= 0:
            self.__precio = precio

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data: dict):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self) -> str:
        return (
            f"ID: {self.__id} | "
            f"Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__precio:.2f}"
        )