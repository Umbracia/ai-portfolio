"""
CSV Data Cleaner
Limpia archivos CSV: elimina duplicados, valores vacíos, espacios extra
"""
import csv
import sys


def limpiar_valor(valor):
    """
    Limpia un valor individual: elimina espacios inicio/fin
    
    Args:
        valor (str): Valor a limpiar
    
    Returns:
        str: Valor limpio
    """
    return valor.strip()


def es_email_valido(email):
    """Valida formato email básico"""
    if not email or not email.strip():
        return False
    email = email.strip()
    return "@" in email and "." in email and len(email) > 5


def fila_valida(fila_dict):
    """
    Valida fila: debe tener nombre Y email válido
    """
    nombre = fila_dict.get('nombre', '').strip()
    email = fila_dict.get('email', '').strip()
    
    # Nombre no vacío Y email válido
    if not nombre:
        return False
    if not es_email_valido(email):
        return False
    
    return True


def limpiar_csv(input_file, output_file):
    """
    Limpia CSV: elimina duplicados, filas vacías, espacios extra
    
    Args:
        input_file (str): Ruta archivo CSV sucio
        output_file (str): Ruta archivo CSV limpio
    
    Returns:
        dict: Estadísticas de limpieza
    """
    filas_limpias = []
    filas_vistas = set()  # Para detectar duplicados
    
    stats = {
        'total': 0,
        'duplicados': 0,
        'invalidas': 0,
        'limpias': 0
    }
    
    # LEER CSV SUCIO
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for fila in reader:
                stats['total'] += 1
                
                # 1. VALIDAR: fila no está completamente vacía
                if not fila_valida(fila):
                    stats['invalidas'] += 1
                    continue
                
                # 2. LIMPIAR: eliminar espacios de TODOS los valores
                fila_limpia = {}
                for key, valor in fila.items():
                    fila_limpia[key] = limpiar_valor(valor)
                
                # 3. DETECTAR DUPLICADOS
                # Convertir a tupla para poder usar en set()
                fila_tuple = tuple(fila_limpia.values())
                
                if fila_tuple in filas_vistas:
                    stats['duplicados'] += 1
                    continue
                
                filas_vistas.add(fila_tuple)
                filas_limpias.append(fila_limpia)
                stats['limpias'] += 1
    
    except FileNotFoundError:
        print(f"❌ Error: Archivo '{input_file}' no encontrado")
        return None
    
    # ESCRIBIR CSV LIMPIO
    if filas_limpias:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            # Usar las keys del primer diccionario como headers
            fieldnames = filas_limpias[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(filas_limpias)
        
        print(f"✅ CSV limpiado exitosamente!")
        print(f"   Archivo: {output_file}")
    else:
        print("⚠️  No hay filas válidas para escribir")
    
    return stats


def imprimir_stats(stats):
    """Imprime estadísticas de limpieza"""
    if stats:
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"   Total filas procesadas: {stats['total']}")
        print(f"   Filas limpias: {stats['limpias']}")
        print(f"   Duplicados eliminados: {stats['duplicados']}")
        print(f"   Filas inválidas: {stats['invalidas']}")


if __name__ == "__main__":
    # Archivos por defecto
    input_csv = "test_data.csv"
    output_csv = "clean_data.csv"
    
    # Permitir archivos custom desde línea de comandos
    if len(sys.argv) >= 3:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
    
    print(f"🧹 Limpiando CSV: {input_csv}")
    print("-" * 50)
    
    stats = limpiar_csv(input_csv, output_csv)
    imprimir_stats(stats)