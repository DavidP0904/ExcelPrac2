import pandas as pd
from matplotlib import pyplot as plt

# Leer archivo Excel

archivo_excel = "datos/datos_base.xlsx"
data_hoja = pd.read_excel(archivo_excel, sheet_name="Hoja5")
print(data_hoja)

# Grafica de ejemplo
eje_y = [2, 3, 5, 7, 11]
eje_x = ["A", "B", "C", "D", "E"]
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="blue", label="Datos de ejemplo")
fig.savefig("generados/grafica_ejemplo.png", bbox_inches="tight")

# Graficar datos de la hoja 5
eje_x = data_hoja.iloc[:, 0]  # Asumiendo que la primera columna es el eje X
eje_y = data_hoja.iloc[:, 1]  # Asumiendo que la segunda columna es el eje Y
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="green", label="Datos de Hoja5")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_xticklabels(eje_x, rotation=45)
fig.savefig("generados/grafica_hoja5.png", bbox_inches="tight")