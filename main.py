import requests

def descargar_datos_csv(url: str, dataset: str ):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(dataset, 'wb') as archivo_csv:
                archivo_csv.write(response.content)
            print(f"Los datos fueron descargados correctamente y guardados en {dataset}")
        else:
            print(f"Error al descargar los datos. Error {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error {str(e)}")

url_datos = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
dataset = 'heart_failure_clinical_records_dataset.csv'
descargar_datos_csv(url_datos, dataset)
