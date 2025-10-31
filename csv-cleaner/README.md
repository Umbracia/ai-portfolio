# CSV Data Cleaner 🧹

Script Python profesional para limpiar archivos CSV eliminando duplicados, filas inválidas y espacios extra.

## ✨ Features

- ✅ Elimina filas duplicadas
- ✅ Remueve filas con datos inválidos (email sin @ o .)
- ✅ Limpia espacios extra en todos los campos
- ✅ Valida nombres no vacíos
- ✅ Genera estadísticas de limpieza
- ✅ Soporte UTF-8 (caracteres especiales: ñ, á, é)
- ✅ Uso desde línea de comandos

## 🚀 Instalación
```bash
# Clonar repositorio
git clone https://github.com/Umbracia/ai-portfolio.git
cd ai-portfolio/csv-cleaner

# Activar entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

# No requiere dependencias externas (solo Python 3.11+)
```

## 📖 Uso

### Uso básico
```bash
# Limpiar archivo test_data.csv (genera clean_data.csv)
python csv_cleaner.py
```

### Uso con archivos personalizados
```bash
# Sintaxis: python csv_cleaner.py <input.csv> <output.csv>
python csv_cleaner.py mi_lista_clientes.csv clientes_limpio.csv
```

### Ejemplo output
```
🧹 Limpiando CSV: test_data.csv
--------------------------------------------------
✅ CSV limpiado exitosamente!
   Archivo: clean_data.csv

📊 ESTADÍSTICAS:
   Total filas procesadas: 6
   Filas limpias: 4
   Duplicados eliminados: 1
   Filas inválidas: 1
```

## 🛠️ Tech Stack

- **Python 3.11+**
- **csv** (built-in)
- **sys** (built-in)

## 💼 Use Cases

### Para Negocios
- Limpiar listas de clientes exportadas de CRM
- Preparar datos para importación a plataformas de email marketing
- Depurar bases de datos de contactos

### Para Análisis de Datos
- Pre-procesamiento de datasets
- Limpieza antes de análisis con Pandas
- Preparación de datos para Machine Learning

### Para E-commerce
- Limpiar catálogos de productos
- Validar listas de emails de suscriptores
- Preparar datos para sincronización con inventarios

## 📋 Formato CSV Soportado
```csv
nombre,email,telefono
Juan Perez,juan@gmail.com,5551234567
Maria Lopez,maria@yahoo.com,5559876543
```

**Requisitos:**
- Primera fila debe ser header (nombres columnas)
- Debe incluir columnas `nombre` y `email`
- Encoding UTF-8

## 🔧 Validaciones

El script valida:
- **Nombre:** No puede estar vacío
- **Email:** Debe contener `@` y `.` con al menos 5 caracteres
- **Duplicados:** Detecta filas idénticas

## 📊 Estadísticas

El script genera reporte con:
- Total de filas procesadas
- Filas válidas resultantes
- Duplicados eliminados
- Filas inválidas descartadas

## 🤝 Autor

**Gustavo Torres** - [@Umbracia](https://github.com/Umbracia)

Desarrollador Python especializado en automatización y procesamiento de datos.

## 📝 Licencia

Proyecto educativo - Día 2 del roadmap de 90 días Python/AI.

---

**¿Necesitas personalizar este script?** Contacta para servicios de limpieza de datos automatizada.