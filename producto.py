class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre  ## Atributo privado
        self.__precio = precio  ## Atributo privado
        self.__stock = max(0, stock)  ## No se permite stock negativo

    ## Getter
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    ## Setter restringido (solo modifica stock)
    def modificar_stock(self, nuevo_stock):
        self.__stock = max(0, nuevo_stock)

    ## Métodos especiales para sobrecarga
    def __eq__(self, otro):
        return self.__nombre.lower() == otro.obtener_nombre().lower()

    def __add__(self, otro):
        if self == otro:
            self.__stock += otro.obtener_stock()
        return self

    def __sub__(self, cantidad):
        self.__stock = max(0, self.__stock - cantidad)
        return self
