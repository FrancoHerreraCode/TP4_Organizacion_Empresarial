import pandas as pd
import matplotlib.pyplot as plt
import datetime

# =====================================================================
# SCRIPT DE PRODUCCIÓN - ESCENARIO B (ANÁLISIS DE VENTAS 2024)
# Cátedra: Organización Empresarial - UTN
# =====================================================================

# 1. Lectura reproducible mediante rutas relativas
df = pd.read_csv("datos/dataset_ventas.csv")

# 2. Procesamiento de Indicadores Matemáticos
df["PriceUnit"] = df['LineItemTotal'] / df['OrderQty']
ventas_totales = df["LineItemTotal"].sum()

# 3. Identificación de Producto Estrella
grupo_producto = df.groupby("ProductID")["OrderQty"].sum()
producto_mas_vendido = grupo_producto.idxmax()
unidades_producto_mas_vendido = grupo_producto.max()

# 4. Análisis de Evolución Temporal
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
nuevo_df = df.set_index('OrderDate')
ventas_por_mes = nuevo_df.resample('ME').sum()['LineItemTotal']
ventas_por_mes.index = ventas_por_mes.index.strftime('%Y-%m')

# 5. Salida por consola de control
print("=== INDICADORES PROCESADOS CON ÉXITO ===")
print(f"Ventas Totales Facturadas: ${ventas_totales:,.2f}")
print(f"Producto más vendido (ID): {producto_mas_vendido} ({unidades_producto_mas_vendido} unidades)")
print("\nEvolución de ventas mensuales:")
print(ventas_por_mes.to_string())
