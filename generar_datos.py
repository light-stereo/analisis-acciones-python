import pandas as pd
import numpy as np

np.random.seed(42)

dias = 100

precios = 100 + np.cumsum(np.random.randn(dias))

df = pd.DataFrame({
    "fecha": pd.date_range(start="2023-01-01", periods=dias),
    "precio_cierre": precios
})

df.to_csv("datos/acciones.csv", index=False)

print("Datos generados correctamente")