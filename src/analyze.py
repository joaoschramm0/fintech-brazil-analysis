import pandas as pd

df = pd.read_csv('data/processed/pix_data.csv')

# Calcula a variação pct mensal do valor
valor_pct = df['VALOR'].pct_change() * 100

# Calcula a variação pct mensal da quantidade
qtd_pct = df['QUANTIDADE'].pct_change() * 100

max_valor_pct = valor_pct.max()
max_qtd_pct = qtd_pct.max()

mes_max_valor = df.loc[valor_pct.idxmax(), 'AnoMes']
mes_max_qtd = df.loc[qtd_pct.idxmax(), 'AnoMes']


print(f'Maior variação percentual mensal do valor: {max_valor_pct:.2f}%' f' em {mes_max_valor}')
print(f'Maior variação percentual mensal da quantidade: {max_qtd_pct:.2f}%' f' em {mes_max_qtd}')