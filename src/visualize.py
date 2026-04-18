import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/processed/pix_data.csv')

# Conversões para escalas mais legíveis
df['AnoMes'] = pd.to_datetime(df['AnoMes'])
df['VALOR_TRI'] = df['VALOR'] / 1e12
df_trim = df.resample('QE', on='AnoMes').sum()
df_trim['QUANTIDADE_BI'] = df_trim['QUANTIDADE'] / 1e9

# Datas futuras
future_date = pd.date_range(df_trim.index[-1], periods=5, freq='QE')
future_num = future_date.astype(np.int64) / 10**9

# Tendência
np_num = df_trim.index.astype(np.int64) / 10**9
coef = np.polyfit(np_num, df_trim['VALOR_TRI'], 1)

# Projeção
projection = np.polyval(coef, future_num)

# Helper
quedas = df_trim[df_trim['VALOR_TRI'].pct_change() < 0]

# Gráficos
fig, ax1 = plt.subplots(figsize=(20, 10))

# Valor e projeção
datas_conectadas = pd.DatetimeIndex([df_trim.index[-1]]).append(future_date)
valores_conectados = np.append(df_trim['VALOR_TRI'].iloc[-1], projection)
ax1.plot(datas_conectadas, valores_conectados, color='red', linestyle='--', label='Projeção')
ax1.plot(df_trim.index, df_trim['VALOR_TRI'], color='blue', label='Valor')
ax1.set_ylabel('Valor (R$ trilhões)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.annotate(f'R$ {projection[-1]:.1f}T em 2027', 
             xy=(future_date[-1], projection[-1]),
             xytext=(-100,0),
             textcoords='offset points',
             fontsize=10,
             ha='left')
ax1.scatter(future_date[-1], projection[-1], color='red', zorder=5, s=45)

# Quantidade
ax2 = ax1.twinx()
ax2.plot(df_trim.index, df_trim['QUANTIDADE_BI'], color='gray', label='Quantidade')
ax2.set_ylabel('Quantidade (bilhões)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

ax1.scatter(quedas.index, quedas['VALOR_TRI'], color='darkblue', zorder=5, label='Queda', marker='o', s=45, edgecolor='black')
ax1.legend(loc='upper left')

plt.title('PIX: Volume Financeiro e Quantidade de Transações')
plt.savefig('outputs/pix_volume_quantidade.png')

