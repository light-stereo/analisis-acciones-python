import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/acciones.csv")

df["fecha"] = pd.to_datetime(df["fecha"])

df["MA7"] = df["precio_cierre"].rolling(window=7).mean()
df["MA20"] = df["precio_cierre"].rolling(window=20).mean()

df["retorno"] = df["precio_cierre"].pct_change()

plt.figure()
plt.plot(df["fecha"], df["precio_cierre"], label="Precio")
plt.plot(df["fecha"], df["MA7"], label="MA7")
plt.plot(df["fecha"], df["MA20"], label="MA20")
plt.legend()
plt.title("Precio y Medias Móviles")
plt.savefig("graficos/precios.png")

plt.figure()
plt.hist(df["retorno"].dropna(), bins=30)
plt.title("Distribución de Retornos")
plt.savefig("graficos/retornos.png")

print("Análisis completado")