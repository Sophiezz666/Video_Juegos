import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('videojuegos_dataset.csv')

print("\nPrimeras 5 filas del dataset:")
print(df.head(5))
print("\nInformación del DataSet:")
print(df.info())
print("\nDescripción estadística del DataSet:")
print(df.describe())

print("\nMostarar columnas del DataSet:")
print("\nMostarar por columna Titulo:")
# Seleccionar columnas específicas
print(df['title'])
print("---" * 20)
print("\Mostarar por columnas unidades vendidas y total ganancias:")
print(df[['units_sold', 'total_revenue']])
print("\nMostrar filas por indice")
#Seleccionar filas específicas
print(df.iloc[0:7])

print("\nFiltrar datos por columna")
print("\nFiltrar por genero Simulacion")
print(df[df['genre'] == 'Simulation'])
print("---" * 30)
print("\nFiltrar por score mayor a 90")
print(df[df['metascore'] > 90])

print("\nCreacion nueva columna")
df['revenue_unit'] = df['total_revenue'] / df['units_sold']
print(df.head(5))

print("\nOrdenar y agrupar datos")
print("\nOrdenar descendente por Total de ganancias")
ordenado_total = df.sort_values('total_revenue', ascending=False)
print(ordenado_total)
print("---" * 30)
print("\nAgrupar datos unidades vendidas por  Año de lanzamiento")
unidades_vendidas_año = df.groupby(['platform', 'release_year'])['units_sold'].sum()
print(unidades_vendidas_año)

print("\nManejo de valores nulos")
# Simular un valor nulo en el ingreso total (Índice 1)
df.loc[1, 'total_revenue'] = None 
print(f"Nulos después de simulación: {df['total_revenue'].isnull().sum()}")

# Rellenar nulos
valor_diferencial = 1000000

df['total_revenue'] = df['total_revenue'].fillna(valor_diferencial) 
print(f"El valor nulo se reemplazó por: {valor_diferencial}")
print("\nRecalcular total")
# Recalcular el total con un precio unitario
df['total_revenue'] = df['units_sold'] * 50.0 

print(df.head(5))

print("\nMini Dashboard con graficas")
# Agrupación por Género 
total_por_genero = df.groupby('genre')['total_revenue'].sum() 
# Agrupación por Plataforma 
total_por_plataforma = df.groupby('platform')['total_revenue'].sum()

# Creación de Subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# Gráfico Ventas por Género
total_por_genero.plot( kind='bar', ax=axes[0], title='Ventas por Género (Top 5)')
axes[0].set_xlabel('Género')
axes[0].set_ylabel('Total de Ingresos')

# Gráfico por Plataforma 
total_por_plataforma.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', 
    title='Participación por Plataforma',
    ylabel='', xlabel='')

plt.tight_layout()
plt.show()