from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
from dataProcessing import converted_data


def __init__():
    credentials_path = "credenciais_google.json"
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    df = pd.DataFrame(converted_data)

    # Enviar o DataFrame para o BigQuery
    try:
        if converted_data:
            table_id = "prime-odyssey-387405.projeto.projeto_data"
            pandas_gbq.to_gbq(df, table_id, project_id=credentials.project_id, credentials=credentials, if_exists="append")
        else:
            raise f'Os dados convertidos são nulos!'
        print('Dados enviados com sucesso!')
    except Exception as error:
        raise f'Erro {error}'

__init__()