# Hacemos una lista de productos
productos = [
    {"nombre": "Producto A", "precio": 10, "stock": 50},
    {"nombre": "Producto B", "precio": 20, "stock": 30},
    {"nombre": "Producto C", "precio": 15, "stock": 40},
]

# Ordenamos por precio
def ordenar_por_precio(productos):
    return sorted(productos, key=lambda x: x["precio"])

# Calculamos el stock
def calcular_stock(productos, movimientos):
    inventario = {producto["nombre"]: producto["stock"] for producto in productos}
    
    for movimiento in movimientos:
        producto_nombre = movimiento["nombre"]
        cantidad = movimiento["cantidad"]
        
        if producto_nombre in inventario:
            inventario[producto_nombre] += cantidad
        else:
            print(f"El producto {producto_nombre} no está en el inventario")
    
    # Actualizamos el stock en la lista de productos
    for producto in productos:
        producto["stock"] = inventario[producto["nombre"]]
    
    return productos

# Lista de movimientos
movimientos = [
    {"nombre": "Producto A", "cantidad": 100},  # Entrada de 10 unidades
    {"nombre": "Producto B", "cantidad": -5},  # Salida de 5 unidades
    {"nombre": "Producto C", "cantidad": 20},  # Entrada de 20 unidades
]

# Ordenamos los productos por precio
productos_ordenados = ordenar_por_precio(productos)
print("Productos ordenados por precio:")
for producto in productos_ordenados:
    print(producto)

# Calculamos el stock restante después de los datos introucidos
productos_actualizados = calcular_stock(productos, movimientos)
print("\nStock actualizado:")
for producto in productos_actualizados:
    print(producto)
