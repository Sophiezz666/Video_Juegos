
from Videojuego import VideoJuego
import pandas as pd

class muestra_csv:
    def __init__(self):
        self.df = pd.read_csv("videojuegos_dataset.csv")
    
    def primeros_5(self):
        print("primeros 5:")
        print(self.df.head(5))  
        return self.df.head(5)
    
    def informacion_dataset(self):
        print("informacion dataset:")
        print(self.df.info())
        return self.df.info()
    
    def descripcion_estadistica(self):
        print("informacion detallada:")  
        print(self.df.describe())
        return self.df.describe()
    
    def mostrar_columnas(self):
        print("muestra de columnas:")
        print(list(self.df.columns))
        return list(self.df.columns)
    
    def mostrar_columna_titulo(self):
        print(self.df['title']) 
        return self.df['title']
    
    def mostrar_fila_indice(self, inicio=0, fin=7):
        print(f"Mostrando filas {inicio} a {fin-1}:")
        print(self.df.iloc[inicio:fin])
        return self.df.iloc[inicio:fin]
    
    def filtrar_genero(self, genero='Simulation'): 
        print(f"muestra por genero: {genero}")
        res = self.df[self.df['genre'] == genero]
        print(f"Encontrados {len(res)} videojuegos del género {genero}")
        return res
    
    # Métodos adicionales para el menú
    def menu_mostrar_filas_indice(self):
        print("\n--- Mostrar Filas por Índice ---")
        try:
            inicio = int(input("Índice inicial (desde 0): "))
            fin = int(input("Índice final (excluido): "))
            
            if 0 <= inicio < fin <= len(self.df):
                return self.mostrar_fila_indice(inicio, fin)
            else:
                print(f"Índices fuera de rango. El dataset tiene {len(self.df)} filas")
        except ValueError:
            print("Por favor ingrese números válidos")
    
    def menu_filtrar_por_genero(self):
        print("\n--- Filtrar por Género ---")
        print("Géneros disponibles:", list(self.df['genre'].unique())[:10], "...")
        
        genero = input("Ingrese el género a filtrar: ").strip()
        if genero:
            return self.filtrar_genero(genero)
        else:
            print("No se ingresó un género válido")
    
    def mostrar_resumen(self):
        print("\n" + "="*50)
        print("RESUMEN COMPLETO DEL DATASET")
        print("="*50)
        self.primeros_5()
        self.informacion_dataset()
        self.descripcion_estadistica()
        self.mostrar_columnas()
        self.mostrar_columna_titulo()
        self.mostrar_fila_indice()
        self.filtrar_genero()
    
    def crear_videojuegos_objetos(self):
        videojuegos = []
        for _, fila in self.df.iterrows():
            videojuego = VideoJuego(
                id=fila['id'],
                title=fila['title'],
                genre=fila['genre'],
                platform=fila['platform'],
                release_year=fila['release_year'],
                units_sold=fila['units_sold'],
                metascore=fila['metascore'],
                total_revenue=fila['total_revenue']
            )
            videojuegos.append(videojuego)
        print(f"Se crearon {len(videojuegos)} objetos VideoJuego")

def crear_analizador():
    return muestra_csv()



