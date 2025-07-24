from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self._productos = []  ## Lista protegida, COMPOSICIÓN

    def obtener_nombre(self):
        return self.__nombre

    def obtener_costo_delivery(self):
        return self.__costo_delivery

    def buscar_producto(self, nombre_producto):
        for p in self._productos:
            if p.obtener_nombre().lower() == nombre_producto.lower():
                return p
        return None

    def ingresar_producto(self, nombre, precio, stock=0):
        ## Para Restaurante el stock siempre es 0
        if isinstance(self, Restaurante):
            stock = 0

        nuevo = Producto(nombre, precio, stock)
        existente = self.buscar_producto(nombre)

        if existente:
            if not isinstance(self, Restaurante):
                existente + nuevo  ## Colaboración vía sobrecarga
        else:
            self._productos.append(nuevo)

    def realizar_venta(self, nombre_producto, cantidad):
        pass  ## A implementar en subclases

    def listar_productos(self):
        pass  ## A implementar en subclases


class Restaurante(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        ## No se valida stock, ni se modifica
        print(f"Se vendió {cantidad} de {nombre_producto} (Restaurante)")

    def listar_productos(self):
        salida = f"Productos en {self.obtener_nombre()}:\n"
        for p in self._productos:
            salida += f"- {p.obtener_nombre()}: ${p.obtener_precio()}\n"
        return salida


class Supermercado(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        prod = self.buscar_producto(nombre_producto)
        if prod:
            disponible = prod.obtener_stock()
            vendido = min(cantidad, disponible)
            prod - vendido
            print(f"Se vendieron {vendido} de {nombre_producto}")
        else:
            print("Producto no disponible")

    def listar_productos(self):
        salida = f"Productos en {self.obtener_nombre()}:\n"
        for p in self._productos:
            stock = p.obtener_stock()
            extra = " - Pocos productos disponibles" if stock < 10 else ""
            salida += f"- {p.obtener_nombre()}: ${p.obtener_precio()}, Stock: {stock}{extra}\n"
        return salida


class Farmacia(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print("No se pueden vender más de 3 unidades por producto (Farmacia)")
            return

        prod = self.buscar_producto(nombre_producto)
        if prod:
            disponible = prod.obtener_stock()
            vendido = min(cantidad, disponible)
            prod - vendido
            print(f"Se vendieron {vendido} de {nombre_producto}")
        else:
            print("Producto no disponible")

    def listar_productos(self):
        salida = f"Productos en {self.obtener_nombre()}:\n"
        for p in self._productos:
            precio = p.obtener_precio()
            texto = f"- {p.obtener_nombre()}: ${precio}"
            if precio > 15000:
                texto += " - Envío gratis al solicitar este producto"
            salida += texto + "\n"
        return salida
