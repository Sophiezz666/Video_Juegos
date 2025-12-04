import pandas as pd
import matplotlib.pyplot as plt
from VideoJuego import VideoJuego

class Metodos(VideoJuego):
    def mostrar_dos_columnas(self, units_sold, total_revenue): # Se especifican las columnas a mostrar
        print(f"\n---Mostrar columnas especificas: {units_sold} y {total_revenue}---") # Mensaje de encabezado
        return self.df[[units_sold, total_revenue]].head(50) # Retorna los 50 primeros registros de las columnas especificadas
        
    def filtrar_metascore(self, score_minimo=90): # Se especifica el score minimo para filtrar
        print(f"\n---Juegos con MetaScore > {score_minimo} ---") # Mensaje encabezado
        return self.df[self.df['metascore'] > score_minimo].head(50) # Retorna los 50 primeros registros que cumplen la condicion
    
    def crear_columna(self): # Crea nueva columna revenue_unit
        print(f"\n---Crear columna revenue_unit") # Encabezado
        self.df['revenue_unit'] = self.df['total_revenue']/self.df['units_sold'] # Calculo entre columnas para total de ganancias por unidad
        return self.df[['title', 'revenue_unit']].head(50) # Retorna primeros 50 registro de la columna creada
    
    def ordenar_por_ganancias(self, total_revenue): # Ordena por total de ganancias
        print(f"\n---Ordenar por total_revenue---") # Encabezado
        df_ordenado = self.df.sort_values('total_revenue', ascending=False) # Ordena el df por el total de ganancias mayor a menor
        return df_ordenado[['title', total_revenue]].head(50) # Retorna los 50 primeros registros del df ordenado
    
    def agrupar_unidades_vendidas_año(self): # Agrupa unidades vendidas por año de lanzamiento
        print(f"\n---Agrupar ganancias anuales por platforma---") # Mensade encabezado
        unidades_vendidas_año = self.df.groupby(['plataform','release_year'])['units_sold'].sum() # Agrupa datos unidades vendidas por  Año de lanzamiento 
        return unidades_vendidas_año.head(50) # Retorna primeros 50 registros del  agrupamiento
    
    def simular_nulo(self, indice=1, columna='total_revenue'): # Simula valor nulo por incdice y columna
        self.df.loc[indice, columna] = None # Accede a la fila por indice y columna para asignar valor nulo
        nulos_despues = self.df[columna].isnull().sum() # Cuenta valores nulos en la columna
        print(f"\n---Simular Null ---") # Encabezado
        return f"Nulos en '{columna}' después de simular{indice}: {nulos_despues}" # Retorna cantidad de nulos despues de la simulacion
    
    def rellenar_nulos(self, columna='total_revenue', valor_diferencial = 1000000):
        print(f"\n---Rellenar valores nulos---") # Encabezado
        self.df[columna] = self.df[columna].fillna(valor_diferencial) # Rellena valores nulos con el valor diferencial especificado
        return f"El valor nulo se reemplazó por: {valor_diferencial}" # Retorna mensaje de reemplazo confirmado