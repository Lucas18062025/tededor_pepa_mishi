import pandas as pd

# Crear tabla de productos
productos = {
    "Producto": ["Remera", "Gorra", "Zapatilla"],
    "Precio": [1500, 1200, 3500],
    "Stock": [20, 15, 10]
}

df = pd.DataFrame(productos)
print("Inventario inicial:")
print(df)

# Pedido simulado
pedido = {"Remera": 2, "Gorra": 1}

total = 0
for producto, cantidad in pedido.items():
    precio_unitario = df.loc[df["Producto"] == producto, "Precio"].values[0]
    total += precio_unitario * cantidad
    # Actualizar el stock
    df.loc[df["Producto"] == producto, "Stock"] -= cantidad

print("\nPedido realizado:")
print(pedido)
print("Total a pagar: $", total)
print("\nInventario actualizado:")
print(df)
df.to_csv("inventario.csv", index=False)
print("\nInventario actualizado guardado en inventario.csv")
# Leer el inventario desde el archivo CSV