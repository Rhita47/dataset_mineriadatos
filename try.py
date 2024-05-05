import pandas as pd
import re

# Ruta al archivo CSV
file_path = 'C:/Users/anton/Downloads/StudentsPerformance.csv'


# Función para limpiar y separar los datos del archivo CSV
def load_and_clean_data(file_path):
    # Leer las líneas del archivo como texto para manejar la estructura compleja
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Preparar los datos para crear un DataFrame
    data = []
    headers = lines[0].strip().strip('"').split('","')  # Limpiar y dividir el encabezado
    headers[0] = 'gender'  # Corregir el primer encabezado que tiene un problema
    headers.insert(1, 'race/ethnicity')  # Insertar el encabezado faltante

    # Procesar cada línea de datos
    for line in lines[1:]:
        # Limpiar y dividir cada línea por comillas y comas
        processed_line = re.sub(r'^"|"$', '', line.strip()).split('","')
        if len(processed_line) == 7:  # Si la división no es correcta debido a problemas de formato
            first_fields = processed_line[0].split(',', 1)
            data.append([first_fields[0], first_fields[1]] + processed_line[1:])
        else:
            data.append(processed_line)

    # Crear DataFrame con los datos y encabezados limpios
    df = pd.DataFrame(data, columns=headers)
    for column in df.columns:
        df[column] = df[column].str.strip('"')  # Limpiar comillas adicionales en los datos

    # Convertir columnas de puntuaciones a numéricas
    score_columns = ['math score', 'reading score', 'writing score']
    for col in score_columns:
        df[col] = pd.to_numeric(df[col])
    
    return df

df = load_and_clean_data(file_path)

# Mostrar las primeras filas del DataFrame limpio
print(df.head())
