# API para canalizar datos desde Google Cloud Storage hacia BigQuery
Proyecto de Google Cloud Platform (GCP). Incluye: 
* Script Python para crear en local y en formato CSV datos simulados de: departments, jobs, y employees.
* Aplicación API Rest basada en FastAPI para cargar archivos locales en formato CSV a un bucket de Google Cloud Storage (GCS), cargar por lotes tablas en BigQuery a partir de archivos CSV en GCP y realizar consultas SQL de tablas en BigQuery.
* Despliegue de aplicación API como una imagen Docker usando Google App Engine.

## 1. Detalle de archivos y carpetas:

| Archivo/Carpeta  | Descripción |
| ------------- | ------------- |
| data_simulated  | Contiene el script python `create_csv_files.py` que genera datos simulados y aleatorios (usando la libreria faker) y los almacena en la ruta local `csv_files`.  |
| main.py  | Implementación de servicio API Rest usando librerías FastAPI. La API permite el cargue de archivos CSV a un bucket en GCS, el cargue por lotes de los datos contenidos en archivos CSV dentro de un bucket de GCS para poblar las tablas (del mismo nombre) en BigQuery y la ejecución de una consulta SQL a varias tablas en BigQuery.   |
| app.yaml  | Archivo con la configuración para el despliegue del Docker que publica el servicio API Rest.  |
| requirements.txt  | Dependencias de librerías usadas en la implementación.  |

## 2. Diagrama de arquitectura:


## 3. Pre-requisitos:


## 4. Set up:



## 5. API tests:
Página para realizar pruebas de invocación a los diferentes endpoints que componen la API: https://api-csv-to-bigquery.uc.r.appspot.com/docs

## 6. Próximos pasos:



