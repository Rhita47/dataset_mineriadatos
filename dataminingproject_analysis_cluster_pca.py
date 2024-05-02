import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Ruta del archivo CSV
file_path = 'C:/Users/anton/OneDrive - Universidad Alfonso X el Sabio/Universidad/UAX/2ºGrado/2_cuatrimestre/Mineria_Datos/Trabajos/student_performance.csv'

# Leer el archivo CSV
data = pd.read_csv(file_path, delimiter=';')

# Codificación de variables categóricas
encoder = LabelEncoder()
categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])
    # Obtener los valores numéricos que representan cada valor
    label_mapping = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))
    print(f"Valores numéricos para la columna '{col}': {label_mapping}")

# Estandarización de puntuaciones
scaler = StandardScaler()
score_columns = ['math score', 'reading score', 'writing score']
data[score_columns] = scaler.fit_transform(data[score_columns])

# Verificación final del preprocesamiento
data_head_preprocessed = data.head()

print(data_head_preprocessed)
