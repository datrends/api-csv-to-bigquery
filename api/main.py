from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from google.cloud import storage 
from google.cloud import bigquery
import os
import sys

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home API Hired Employees (GPC)"}


@app.post("/file_upload")
def upload(file: UploadFile = File(...)):

    storage_client = storage.Client()

    bucket_name = "api-csv-to-bigquery_raw_bucket"
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file.filename)
    
    try:
        contents = file.file.read()
        with blob.open('wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "Hubo un error al cargar el archivo."}
    finally:
        file.file.close()

    return {"message": f"Archivo {file.filename} cargado satisfactoriamente"}


@app.get("/batch_load_gcp_to_bq")
def list_blobs():

    storage_client = storage.Client()

    bucket_name = 'api-csv-to-bigquery_raw_bucket'

    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        filename = os.path.splitext(os.path.basename(blob.name))[0]
        #print(f'{blob.name} >> {filename}')
        load_bq_table(bucket_name, filename)


def load_bq_table(bucket_name, table_name):
    schema_list = []
    project_name = 'api-csv-to-bigquery'
    dataset = 'hired_employees'
    table_id = f'{project_name}.{dataset}.{table_name}'
    bucket_uri = f'gs://{bucket_name}'
    csv_uri = f'{bucket_uri}/{table_name}.csv'

    '''Authenticate with BigQuery using service account key (not a recommended approach)'''
    path_to_sa_key = 'sa_key.json'
    bq_client = bigquery.Client().from_service_account_json(path_to_sa_key)

    try:
        print(table_id)
        '''Get the schema of the target table in which the CSV file needs to be loaded'''
        hdw_schema = bq_client.get_table(table_id)
        for field in hdw_schema.schema:
            schema_list.append(bigquery.SchemaField(name=field.name, field_type=field.field_type, mode=field.mode))
                
        '''Load the CSV file in BigQuery'''
        job_config = bigquery.LoadJobConfig()
        job_config.schema = schema_list
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.skip_leading_rows=1
        job_config.field_delimiter = ','
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        job_config.null_marker = ''

        load_job = bq_client.load_table_from_uri(
            csv_uri, table_id, job_config=job_config
        )

        load_job.result() # waits for the load job to finish

        destination_table = bq_client.get_table(table_id)

    except Exception:
        #print(f'Hubo un error al cargar el archivo: tabla <{table_name}> no existe.')
        return {"message": f"Hubo un error al cargar el archivo <{table_name}.csv>: tabla <{table_name}> no existe."}

    #print(f'Archivo <{table_name}.csv> cargado satisfactoriamente a BigQuery. Tabla <{table_name}> con un total de {destination_table.num_rows} registros.')
    return{"message": f"Archivo <{table_name}.csv> cargado satisfactoriamente a BigQuery. Tabla <{table_name}> con un total de {destination_table.num_rows} registros."}