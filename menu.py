# menu_analizador.py - Adaptado para la nueva clase muestra_csv
from funciones import*

def mostrar_menu():
    print("\n" + "="*60)
    print(" MENÚ ANALIZADOR DE VIDEOJUEGOS ")
    print("="*60)
    print("1. Mostrar primeras 5 filas del dataset")
    print("2. Mostrar información del dataset")
    print("3. Mostrar descripción estadística")
    print("4. Mostrar todas las columnas")
    print("5. Mostrar solo columna de títulos")
    print("6. Mostrar filas por índice")
    print("7. Filtrar por género")
    print("8. Mostrar resumen completo")
    print("9. Convertir a objetos VideoJuego")
    print("0. Salir")
    print("="*60)

def menu_objetos_videojuego(analizador):
    print("\n--- Trabajar con Objetos VideoJuego ---")
    videojuegos = analizador.crear_videojuegos_objetos()
    
    if videojuegos:
        print("\nPrimeros 3 videojuegos como objetos:")
        for i, juego in enumerate(videojuegos[:3], 1):
            print(f"{i}. {juego.title} ({juego.release_year})")
            print(f"   Género: {juego.genre}")
            print(f"   Plataforma: {juego.platform}")
            print(f"   Score: {juego.metascore}")
            print(f"   Ventas: {juego.units_sold:,} unidades")
            print()

def main():
    print("🔍 CARGANDO DATASET DE VIDEOJUEGOS...")
    
    try:
        # Crear instancia del analizador
        analizador = crear_analizador()
        print(f"✅ Dataset cargado exitosamente: {len(analizador.df)} registros")
        
        while True:
            mostrar_menu()
            opcion = input("\nSeleccione una opción (0-9): ").strip()
            
            if opcion == "0":
                print("\n¡Gracias por usar el Analizador de Videojuegos! 👋")
                break
            
            elif opcion == "1":
                analizador.primeros_5()
            
            elif opcion == "2":
                analizador.informacion_dataset()
            
            elif opcion == "3":
                analizador.descripcion_estadistica()
            
            elif opcion == "4":
                analizador.mostrar_columnas()
            
            elif opcion == "5":
                analizador.mostrar_columna_titulo()
            
            elif opcion == "6":
                analizador.menu_mostrar_filas_indice()
            
            elif opcion == "7":
                analizador.menu_filtrar_por_genero()
            
            elif opcion == "8":
                analizador.mostrar_resumen()
            
            elif opcion == "9":
                menu_objetos_videojuego(analizador)
            
            else:
                print("⚠️ Opción no válida. Por favor seleccione una opción del 0 al 9.")
            
            # Pausa para que el usuario pueda ver los resultados
            if opcion != "0":
                input("\nPresione Enter para continuar...")
    
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'videojuegos_dataset.csv'")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()