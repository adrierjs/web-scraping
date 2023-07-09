from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
from dataProcessing import convertedData
class SendData:
    def __init__(self):
        self._credentials_path = './credenciais_google.json'
    def sendInData(self):
        _credentials = service_account.Credentials.from_service_account_file(self._credentials_path)
        _df = pd.DataFrame(convertedData)
        # Enviar o DataFrame para o BigQuery
        try:
            if convertedData:
                table_id = "prime-odyssey-387405.projeto.projeto_data"
                pandas_gbq.to_gbq(_df, table_id, project_id=_credentials.project_id, credentials=_credentials,
                                  if_exists="append")
            else:
                raise f'Os dados convertidos são nulos!'
            return 'Dados enviados com sucesso!'
        except Exception as error:
            raise f'Erro {error}'
