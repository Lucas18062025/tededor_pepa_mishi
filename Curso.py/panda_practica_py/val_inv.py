import pandas as pd

# Inventario inicial
productos = {
    "Producto": ["Remera", "Gorra", "Zapatilla"],
    "Precio": [3500, 1200, 3500],
    "Stock": [20, 15, 10]
}

df = pd.DataFrame(productos)
print("Inventario inicial:")
print(df)

# Pedido simulado
pedido = {"Remera": 2, "Gorra": 1, "Campera": 1}  # 'Campera' no está en el inventario
total = 0
errores = []

for producto, cantidad in pedido.items():
    if producto in df["Producto"].values:
        stock_actual = df.loc[df["Producto"] == producto, "Stock"].values[0]
        if cantidad <= stock_actual:
            precio_unitario = df.loc[df["Producto"] == producto, "Precio"].values[0]
            total += precio_unitario * cantidad
            df.loc[df["Producto"] == producto, "Stock"] -= cantidad
        else:
            errores.append(f"No hay suficiente stock de {producto} (solicitado: {cantidad}, disponible: {stock_actual})")
    else:
        errores.append(f"Producto no encontrado: {producto}")

# Mostrar resumen
print("\nPedido procesado:")
print("Total a pagar: $" + str(total))
if errores:
    print("\n⚠️ Problemas encontrados:")
    for error in errores:
        print("-", error)

# Guardar inventario actualizado
df.to_csv("inventario.csv", index=False)
print("\nInventario actualizado guardado en inventario.csv")
# Fin del script