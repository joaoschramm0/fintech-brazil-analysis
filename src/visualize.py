import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/processed/pix_data.csv')

# Conversões para escalas mais legíveis
df['AnoMes'] = pd.to_datetime(df['AnoMes'])
df['VALOR_TRI'] = df['VALOR'] / 1e12
df_trim = df.resample('QE', on='AnoMes').sum()
df_trim['QUANTIDADE_BI'] = df_trim['QUANTIDADE'] / 1e9

# Helper
quedas = df_trim[df_trim['VALOR_TRI'].pct_change() < 0]

# Gráficos
fig, ax1 = plt.subplots(figsize=(20, 10))

ax1.plot(df_trim.index, df_trim['VALOR_TRI'], color='blue', label='Valor')
ax1.set_ylabel('Valor (R$ trilhões)', color='black')
ax1.tick_params(axis='y', labelcolor='black')

ax2 = ax1.twinx()
ax2.plot(df_trim.index, df_trim['QUANTIDADE_BI'], color='gray', label='Quantidade')
ax2.set_ylabel('Quantidade (bilhões)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

ax1.scatter(quedas.index, quedas['VALOR_TRI'], color='darkblue', zorder=5, label='Queda', marker='o', s=45, edgecolor='black')
ax1.legend(loc='upper left')

plt.title('PIX: Volume Financeiro e Quantidade de Transações')
plt.savefig('outputs/pix_volume_quantidade.png')

print(quedas.index)