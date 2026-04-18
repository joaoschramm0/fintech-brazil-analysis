import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/processed/pix_data.csv')

df['AnoMes'] = pd.to_datetime(df['AnoMes'])

df['VALOR_TRI'] = df['VALOR'] / 1e12

df_trim = df.resample('QE', on='AnoMes').sum()

plt.plot(df_trim.index, df_trim['VALOR_TRI'], color='blue', label='Valor')

plt.title('Volume Financeiro PIX por Ano')
plt.ylabel('Valor em Trilhões (R$)')

plt.savefig('outputs/valor_mensal.png')

plt.figure()

df_trim['QUANTIDADE_BI'] = df_trim['QUANTIDADE'] / 1e9

plt.plot(df_trim.index, df_trim['QUANTIDADE_BI'], color='green', label='Quantidade')
plt.title('Quantidade de Transações PIX por Ano')
plt.ylabel('Quantidade em Bilhões')

plt.savefig('outputs/quantidade_mensal.png')
