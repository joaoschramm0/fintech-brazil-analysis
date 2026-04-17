import pandas as pd
import requests

def fetch_series():
    raw_bcb_data = requests.get("https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database=''&$format=json&$select=AnoMes,VALOR,QUANTIDADE")
    db = pd.DataFrame(raw_bcb_data.json()['value'])
    return db

if __name__ == '__main__':
    df = fetch_series()
    df.to_csv('data/raw/pix_data.csv', index=False)
    print('Dados Salvos')