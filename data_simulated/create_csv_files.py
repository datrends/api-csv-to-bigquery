import pandas as pd
from faker import Faker
import random
import os

# Crear la carpeta 'csv_files' en local si no existe
csv_folder_path = 'data_simulated/csv_files/'
os.makedirs(csv_folder_path, exist_ok=True)

# Configuración de Faker para datos simulados
fake = Faker()

# Generar datos para la tabla departments
departments_data = {'department_id': range(1, 11),
                    'department_name': [fake.word() for _ in range(10)]}
departments_df = pd.DataFrame(departments_data)

# Generar datos para la tabla jobs (más de 100 registros)
jobs_data = {'job_id': range(1, 11),
             'job_title': [fake.job() for _ in range(10)]}
jobs_df = pd.DataFrame(jobs_data)

# Generar datos para la tabla employees
employees_data = {'employee_id': range(1, 101),
                  'employee_name': [fake.name() for _ in range(100)],
                  'department_id': [random.choice(range(1, 11)) for _ in range(100)],
                  'job_id': [random.choice(range(1, 11)) for _ in range(100)],
                  'salary': [random.randint(40000, 100000) for _ in range(100)],
                  'hire_date': [fake.date_this_decade() for _ in range(100)]}
employees_df = pd.DataFrame(employees_data)

# Guardar dataframes en archivos CSV
departments_df.to_csv(os.path.join(csv_folder_path, 'departments.csv'), index=False)
jobs_df.to_csv(os.path.join(csv_folder_path, 'jobs.csv'), index=False)
employees_df.to_csv(os.path.join(csv_folder_path, 'employees.csv'), index=False)

# Mostrar las primeras filas de cada tabla
print("Tabla 'departments':")
print(departments_df.head())

print("\nTabla 'jobs':")
print(jobs_df.head())

print("\nTabla 'employees':")
print(employees_df.head())
