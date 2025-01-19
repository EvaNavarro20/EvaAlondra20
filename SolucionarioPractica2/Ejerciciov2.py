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

