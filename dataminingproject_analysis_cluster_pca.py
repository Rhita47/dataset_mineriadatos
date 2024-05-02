import numpy as np
import pandas as pd 

# Ruta del archivo CSV
file_path = 'C:/Users/anton/OneDrive - Universidad Alfonso X el Sabio/Universidad/UAX/2ºGrado/2_cuatrimestre/Mineria_Datos/Trabajos/student_performance.csv'

# Leer el archivo CSV
df = pd.read_csv(file_path)


# Cargar el dataset utilizando ';' como separador
data = pd.read_csv(file_path, delimiter=';')

# Mostrar las primeras filas y la información del dataset nuevamente para confirmar la estructura correcta
data_info_updated = data.info()
data_head_updated = data.head()

data_info_updated, data_head_updated

from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Verificar valores nulos
null_counts = data.isnull().sum()

# 2. Codificación de variables categóricas
encoder = LabelEncoder()
categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# 3. Estandarización de puntuaciones
scaler = StandardScaler()
score_columns = ['math score', 'reading score', 'writing score']
data[score_columns] = scaler.fit_transform(data[score_columns])

# 4. Verificación final del preprocesamiento
data_head_preprocessed = data.head()

null_counts, data_head_preprocessed

print(data.head())