from tienda import Restaurante, Supermercado, Farmacia

## Crear la tienda
tipo = input("Tipo de tienda (restaurante, supermercado, farmacia): ").lower()
nombre = input("Nombre de la tienda: ")
costo = float(input("Costo de delivery: "))

if tipo == "restaurante":
    tienda = Restaurante(nombre, costo)
elif tipo == "supermercado":
    tienda = Supermercado(nombre, costo)
elif tipo == "farmacia":
    tienda = Farmacia(nombre, costo)
else:
    print("Tipo no válido")
    exit()

## Ingreso de productos
while True:
    print("\n--- Ingreso de productos ---")
    nombre_p = input("Nombre del producto: ")
    precio_p = int(input("Precio del producto: "))
    stock_p = input("Stock del producto (Enter para 0): ")
    stock_p = int(stock_p) if stock_p.strip() else 0

    tienda.ingresar_producto(nombre_p, precio_p, stock_p)

    otro = input("¿Deseas ingresar otro producto? (s/n): ")
    if otro.lower() != "s":
        break

## Menú interactivo
while True:
    print("\nOpciones:")
    print("1. Listar productos")
    print("2. Realizar venta")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(tienda.listar_productos())
    elif opcion == "2":
        nombre_v = input("Nombre del producto a vender: ")
        cantidad_v = int(input("Cantidad a vender: "))
        tienda.realizar_venta(nombre_v, cantidad_v)
    elif opcion == "3":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción inválida.")

