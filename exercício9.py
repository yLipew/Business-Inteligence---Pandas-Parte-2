import pandas as pd

df_loja1 = pd.DataFrame({
    'Produto': ['A', 'B'],
    'Estoque': [10, 20]
})

df_loja2 = pd.DataFrame({
    'Produto': ['C', 'D'],
    'Estoque': [15, 25]
})

# Concatenando
df_total = pd.concat([df_loja1, df_loja2])

print(df_total)