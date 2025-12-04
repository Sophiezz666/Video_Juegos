import pandas as pd
import matplotlib.pyplot as plt
from VideoJuego import VideoJuego

class Metodos(VideoJuego):
    def mostrar_dos_columnas(self, units_sold, total_revenue):
        print(f"\n---Mostrar columnas especificas: {units_sold} y {total_revenue}---")
        return self.df[[units_sold, total_revenue]].head(50)
        
    def filtrar_metascore(self, score_minimo=90): 
        print(f"\n---Juegos con MetaScore > {score_minimo} ---")
        return self.df[self.df['metascore'] > score_minimo].head(50)
    
    def crear_columna(self):
        print(f"\n---Crear columna revenue_unit")
        self.df['revenue_unit'] = self.df['total_revnue']/self.df['units_sold']
        return self.df[['title', 'revenue_unit']].head(50)
    
    def ordenar_por_ganancias(self, total_revenue):
        print(f"\n---Ordenar por total_revenue---")
        df_ordenado = self.df.sort_values('total_revenue', ascendig=False)
        return df_ordenado[['tittle', total_revenue]].head(50)
    
    def agrupar_unidades_vendidas_año(self):
        print(f"\n---Agrupar ganancias anuales por platforma---")
        unidades_vendidas_año = self.df.groupby(['platafrm','release_year'])['units_sold'].sum()
        return unidades_vendidas_año.head(50)
    
    def simular_nulo(self, indice=1, columna='total_revenue'):
        self.df.loc[indice, columna] = None
        nulos_despues = self.df[columna].isnull().sum()
        print(f"\n---Simular Null ---")
        return f"Nulos en '{columna}' después de simular{indice}: {nulos_despues}"