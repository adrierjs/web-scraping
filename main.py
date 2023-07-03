from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
from tratamentoDados import data_convertidos

credentials_path = "credenciais_google.json"

credentials = service_account.Credentials.from_service_account_file(credentials_path)


df = pd.DataFrame(data_convertidos)

# Enviar o DataFrame para o BigQuery
table_id = "prime-odyssey-387405.projeto.projeto_data"
pandas_gbq.to_gbq(df, table_id, project_id=credentials.project_id, credentials=credentials, if_exists="append")
