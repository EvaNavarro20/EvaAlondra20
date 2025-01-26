ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

print("Listado de ventas:")
for i in ventas:
    fecha = i["fecha"]
    producto = i["producto"]
    cantidad = i["cantidad"]
    precio = i["precio"]
    promocion = "Sí" if i["promocion"] else "No"
    print(f"Fecha: {fecha} | Producto: {producto} | Cantidad: {cantidad} | Precio: S/.{precio:.2f} | Promoción: {promocion}")

def agregar_producto(ventas):
    nuevo_producto = {}
    nuevo_producto["fecha"] = input("Ingresar la fecha (dd-mm-aaaa): ")
    nuevo_producto["producto"] = input("Ingresar el nombre del producto: ")
    while True:
      try:
        nuevo_producto["cantidad"] = int(input("Ingresar la cantidad: "))
        break
      except ValueError:
        print("Ingrese un valor numérico para la cantidad.")
    while True:
      try:
        nuevo_producto["precio"] = float(input("Ingresar el precio: "))
        break
      except ValueError:
        print("Ingresar un valor numérico para el precio.")
    while True:
      promocion = input("¿Tiene promoción? (si/no): ").lower()
      if promocion in ["si", "no"]:
          nuevo_producto["promocion"] = promocion == "si"
          break
      else:
          print("Respuesta incorrecta. Deber ingresar: 'si' o 'no'.")

    ventas.append(nuevo_producto)
    return ventas

ventas = agregar_producto(ventas)

print("Listado de ventas actualizado:")
for venta in ventas:
    fecha = venta["fecha"]
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    promocion = "Sí" if venta["promocion"] else "No"
    print(f"Fecha: {fecha} | Producto: {producto} | Cantidad: {cantidad} | Precio: S/.{precio:.2f} | Promoción: {promocion}")

def calcular_sumatotal_ventas(ventas):
  total_ventas = 0
  
  for venta in ventas:
    total_ventas += venta["cantidad"] * venta["precio"]
  return total_ventas

total = calcular_sumatotal_ventas(ventas)
print(f"La suma total de las ventas es: S/.{total:.2f}")

def promediodeventas(ventas):

    total_ventas = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    promedio_ventas = total_ventas / len(ventas)
    return promedio_ventas

promedio = promediodeventas(ventas)
print(f"El promedio de ventas es: S/.{promedio:.2f}")

def obtenercant(venta):
    return venta["cantidad"]

productomasvend = max(ventas, key=obtenercant)
print(f"El producto con más unidades vendidas es: {productomasvend['producto']} con {productomasvend['cantidad']} unidades.")

print("Listado de productos:")
for venta in ventas:
    producto = venta["producto"]
    print(producto)

