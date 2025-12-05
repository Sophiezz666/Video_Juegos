import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from VideoJuego import VideoJuego
#
class Metodos(VideoJuego):
    def __init__(self, archivo_csv):
        super().__init__(archivo_csv)
        
    #Clase para analizar y procesar datos de videojuegos

        # Obtener el dataframe desde esa clase
    def mostrar_info_basica(self):
        #"Muestra información básica del dataset"
        print("\n" + "="*60)
        print("Información dataset")
        print("="*60)
        
        print(self)
        print("\nPrimeras 5 filas del dataset:")
        print(self.df.head(5))
        
        print("\nInformación del DataSet:")
        print(self.df.info())
        
        print("\nseleccion columna dataset:")
        print(self.df.describe())
        
        print(f"\nColumnas disponibles: {list(self.df.columns)}")
        print(f"Total de juegos: {len(self.df)}")
        print(f"Años cubiertos: {self.df['release_year'].min()} - {self.df['release_year'].max()}")
    
    def seleccionar_datos(self):
        """Muestra ejemplos de selección de datos"""
        print("\n" + "="*60)
        print("EJEMPLOS DE SELECCIÓN DE DATOS")
        print("="*60)
        
        print("\nMostrar por columna Título (primeros 10):")
        print(self.df['title'].head(10))
        print("-" * 40)
   
        print("\nMostrar columnas Unidades vendidas y Ganancias totales (primeros 50):")
        print(self.mostrar_dos_columnas())

        print("\nMostrar filas por índice (0-6):")
        print(self.df.iloc[0:7])
    
    def filtrar_datos(self, genero=None ):
        
        #Filtra datos según criterios especificados
        print("\n" + "="*60)
        print("FILTRADO DE DATOS")
        print("="*60)
        
        df_filtrado = self.df.copy()
        
        if genero:
            print(f"\nFiltrar por género '{genero}':")
            df_filtrado = df_filtrado[df_filtrado['genre'] == genero]
            print(f"Encontrados {len(df_filtrado)} juegos de {genero}")
            print(df_filtrado[['title', 'platform', 'release_year', 'metascore']].head(10))
        
        print("\nFiltrado por metascore mayor de 90")
        print(self.filtrar_metascore(90))
        
        return df_filtrado if any([genero ]) else None
    
    def crear_metricas(self):
        #Crea nuevas métricas y columnas calculadas
        print("\n" + "="*60)
        print("CREACIÓN DE NUEVAS MÉTRICAS")
        print("="*60)
        
        print("\nCrear nueva columna Total ganancias por unidad (Primeros 50):")
        print(self.crear_columna())
        
    def ordenar_y_agrupar(self):
        """Realiza operaciones de ordenamiento y agrupación"""
        print("\n" + "="*60)
        print("ORDENAMIENTO Y AGRUPACIÓN DE DATOS")
        print("="*60)
        print("\n---Ordenar por total_revenue---") 
        print(self.ordenar_por_ganancias())
        print(f"\n---Agrupar ganancias anuales por plataforma---")
        print(self.agrupar_unidades_vendidas_año())
     
    def manejar_valores_nulos(self):
        # Maneja valores nulos en el dataset
        print("\n" + "="*60)
        print("MANEJO DE VALORES NULOS")
        print("="*60)

        print("\nSimulacion de valor nulo en Total ganancias")
        print(self.simular_nulo(indice=1, columna='total_revenue'))
        print(self.rellenar_nulos(columna='total_revenue', valor_diferencial = 1000000))
        
    
    def generar_dashboard(self):
        #"Genera un dashboard con gráficos"
        print("\n" + "="*60)
        print("GENERANDO DASHBOARD DE ANÁLISIS")
        print("="*60)
        
        # Preparar datos
        total_por_genero = self.df.groupby('genre')['total_revenue'].sum().sort_values(ascending=False)
        total_por_plataforma = self.df.groupby('platform')['total_revenue'].sum()
        unidades_por_año = self.df.groupby('release_year')['units_sold'].sum()
        
        # Crear figura con múltiples subplots
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        fig.suptitle('Dashboard de Análisis de Videojuegos', fontsize=16, fontweight='bold')
        
        # Gráfico 1: Ventas por Género (Top 10)
        total_por_genero.head(10).plot(kind='bar', ax=axes[0, 0], color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Top 10 Géneros por Ingresos Totales', fontweight='bold')
        axes[0, 0].set_xlabel('Género')
        axes[0, 0].set_ylabel('Ingresos Totales (en miles de millones)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        axes[0, 0].grid(axis='y', alpha=0.3)
        
        # Gráfico 2: Participación por Plataforma
        total_por_plataforma.plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%', 
                                  colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
        axes[0, 1].set_title('Distribución de Ingresos por Plataforma', fontweight='bold')
        axes[0, 1].set_ylabel('')
        
        # Gráfico 3: Unidades vendidas por año
        unidades_por_año.plot(kind='line', ax=axes[1, 0], marker='o', color='green', linewidth=2)
        axes[1, 0].set_title('Evolución de Unidades Vendidas por Año', fontweight='bold')
        axes[1, 0].set_xlabel('Año de Lanzamiento')
        axes[1, 0].set_ylabel('Unidades Vendidas (en millones)')
        axes[1, 0].grid(alpha=0.3)
        axes[1, 0].fill_between(unidades_por_año.index, unidades_por_año.values, alpha=0.3, color='green')
        
        # Gráfico 4: Relación entre Metascore y Unidades Vendidas
        scatter = axes[1, 1].scatter(self.df['metascore'], self.df['units_sold'] / 1000000, 
                                     c=self.df['release_year'], cmap='viridis', alpha=0.6, s=50)
        axes[1, 1].set_title('Relación: Metascore vs Unidades Vendidas', fontweight='bold')
        axes[1, 1].set_xlabel('Metascore')
        axes[1, 1].set_ylabel('Unidades Vendidas (millones)')
        axes[1, 1].grid(alpha=0.3)
        
        # Añadir barra de color para el año
        cbar = plt.colorbar(scatter, ax=axes[1, 1])
        cbar.set_label('Año de Lanzamiento')
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar algunas estadísticas
        print("\nEstadísticas Clave:")
        print(f"- Total de ingresos: ${self.df['total_revenue'].sum():,.2f}")
        print(f"- Total de unidades vendidas: {self.df['units_sold'].sum():,.0f}")
        print(f"- Juego con mayor ingresos: {self.df.loc[self.df['total_revenue'].idxmax(), 'title']}")
        print(f"- Juego con mejor metascore: {self.df.loc[self.df['metascore'].idxmax(), 'title']} ({self.df['metascore'].max()}/100)")
    
    def generar_reporte_completo(self):
        
        print("\n" + "="*60)
        print("REPORTE COMPLETO DE ANÁLISIS DE VIDEOJUEGOS")
        print("="*60)
        
        self.mostrar_info_basica()
        self.seleccionar_datos()
        
        # Ejemplos de filtrado
        self.filtrar_datos('Simulation')
        
        self.crear_metricas()
        self.ordenar_y_agrupar()
        self.manejar_valores_nulos()
        
        # Resumen final
        print("\n" + "="*60)
        print("RESUMEN FINAL")
        print("="*60)
        
        print(f"\nDistribución por plataforma:")
        distribucion_plataforma = self.df['platform'].value_counts()
        for plataforma, count in distribucion_plataforma.items():
            porcentaje = (count / len(self.df)) * 100
            print(f"  {plataforma}: {count} juegos ({porcentaje:.1f}%)")
        
        print(f"\nDistribución por género (Top 5):")
        distribucion_genero = self.df['genre'].value_counts().head(5)
        for genero, count in distribucion_genero.items():
            porcentaje = (count / len(self.df)) * 100
            print(f"  {genero}: {count} juegos ({porcentaje:.1f}%)")
        
        print(f"\nAño con más lanzamientos: {self.df['release_year'].mode().values[0]}")
        print(f"Metascore promedio: {self.df['metascore'].mean():.1f}/100")
        print(f"Unidades vendidas promedio: {self.df['units_sold'].mean():,.0f}")


    def mostrar_dos_columnas(self): # Se especifican las columnas a mostrar
        print(f"\n---Mostrar columnas especificas: {'units_sold'} y {'total_revenue'}---") # Mensaje de encabezado
        return self.df[['units_sold', 'total_revenue']].head(50) # Retorna los 50 primeros registros de las columnas especificadas
        
    def filtrar_metascore(self, score_minimo=90): # Se especifica el score minimo para filtrar
        print(f"\n---Juegos con MetaScore > {score_minimo} ---") # Mensaje encabezado
        return self.df[self.df['metascore'] > score_minimo].head(50) # Retorna los 50 primeros registros que cumplen la condicion
    
    def crear_columna(self): # Crea nueva columna revenue_unit
        print(f"\n---Crear columna revenue_unit") # Encabezado
        self.df['revenue_unit'] = self.df['total_revenue']/self.df['units_sold'] # Calculo entre columnas para total de ganancias por unidad
        return self.df[['title', 'revenue_unit']].head(50) # Retorna primeros 50 registro de la columna creada
    
    def ordenar_por_ganancias(self): # Ordena por total de ganancias
        print("\n---Ordenar por total_revenue---") # Encabezado
        df_ordenado = self.df.sort_values('total_revenue', ascending=False) # Ordena el df por el total de ganancias mayor a menor
        return df_ordenado[['title', 'total_revenue']].head(50) # Retorna los 50 primeros registros del df ordenado
    
    def agrupar_unidades_vendidas_año(self): # Agrupa unidades vendidas por año de lanzamiento
        print("\n---Agrupar ganancias anuales por plataforma---") # Mensade encabezado
        unidades_vendidas_año = self.df.groupby(['platform','release_year'])['units_sold'].sum() # Agrupa datos unidades vendidas por  Año de lanzamiento 
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
