from VideoJuego import VideoJuego
from metodos import Metodos
def main():
  
    
    # Crear instancia del analizador
    analizador = Metodos('videojuegos_dataset.csv')
    # Generar reporte completo
    analizador.generar_reporte_completo()
    
    # Generar dashboard
    analizador.generar_dashboard()
    
    print("\n" + "="*60)
    print("ANÁLISIS COMPLETADO")
    print("="*60)
    print("El análisis incluye:")
    print("1. Información básica del dataset")
    print("2. Filtrado y selección de datos")
    print("3. Creación de nuevas métricas")
    print("4. Ordenamiento y agrupación")
    print("5. Manejo de valores nulos")
    print("6. Dashboard visual interactivo")
    print("7. Reporte estadístico completo")
    
    
    
main()