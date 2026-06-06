import pandas as pd
df = pd.read_csv("datos/dataset_ventas.csv")
df["PriceUnit"] = df['LineItemTotal'] / df['OrderQty']
print(f"Ventas Totales: ${df['LineItemTotal'].sum():,.2f}")
