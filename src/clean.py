import pandas as pd

df = pd.read_csv('data/raw/pix_data.csv')

df['AnoMes'] = pd.to_datetime(df['AnoMes'], format='%Y%m')

df_ok = df.groupby('AnoMes').sum().reset_index()

df_ok.to_csv('data/processed/pix_data.csv', index=False)




