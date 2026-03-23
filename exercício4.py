import pandas as pd

df = pd.DataFrame({
    'Sede A': [1000, 2000, 1500],
    'Sede B': [800, 1200, 700]
})

# 1. Total de vendas
df['Total Vendas'] = df['Sede A'] + df['Sede B']

# 2. Imposto (10% da Sede A)
df['Imposto'] = df['Sede A'] * 0.10

print(df)