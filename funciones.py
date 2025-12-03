from Videojuego import VideoJuego

import pandas  as pd

df = pd.read_csv("videojuegos_dataset.csv")


def prinmeros_5(self):
    print("primeros 5:")
    print(self.df.head[0:5])
    return self.df.head[0:5]

def infomracion_dataset(self):
    print("informacion dataset:")
    print(self.df.info())
    return self.df.info()
def descripcion_estadistica(self):
    print("infomracion detallada:")
    print(self.df.describe())
    return self.df.describe()
def mostrar_columnas(self):
    print("muestra de columnas:")
    print(list(self.df.columns))
    return list(self.df.columns)
def mostrar_columna_titulo(self):
    print(self.df['tittle'])
    return self.df['tittle']
def mostrar_fila_indice(self, inicio = 0, fin = 7):
    print(self.df.iloc[inicio: fin])
    return self.df.iloc[inicio:fin]
def filtrar_genero(self, genero = 'simulacion'):
    print(f"muestra por genero: {genero}")
    res = self.df[self.df['genre'] == genero]
    return res



