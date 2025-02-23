import csv

# Función para limpiar el archivo y extraer solo las columnas de Latitud y Longitud
def clean_and_create_map_csv(txt_filename, csv_filename):
    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()

    # Filtrar solo las líneas que contienen los datos de tipo 'Fix'
    relevant_lines = [line.strip() for line in lines if line.startswith('Fix')]

    # Escribir los datos relevantes en un archivo CSV (solo latitud y longitud)
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Escribir las cabeceras del CSV: 'Latitude', 'Longitude'
        writer.writerow(['Latitude', 'Longitude'])
        
        # Procesar cada línea y extraer los datos de latitud y longitud
        for line in relevant_lines:
            data = line.split(',')
            
            # Extraer latitud y longitud
            latitude = data[2]  # La columna de latitud (índice 2)
            longitude = data[3]  # La columna de longitud (índice 3)
            
            # Escribir la fila con latitud y longitud
            writer.writerow([latitude, longitude])

# Usar el script para limpiar y crear el CSV para Google My Maps
txt_filename = 'gnss_log_2025_02_19_13_09_33.txt'  # Nombre del archivo .txt
csv_filename = 'gnss_data_map.csv'  # Nombre del archivo CSV resultante

clean_and_create_map_csv(txt_filename, csv_filename)
