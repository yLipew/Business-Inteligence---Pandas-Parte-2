import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno'],
    'CPF': ['123', '456'],
    'Telefone': ['9999-9999', '8888-8888']
})

# Removendo coluna CPF
del df['CPF']

# Removendo coluna Telefone e armazenando
telefone_removido = df.pop('Telefone')

print(df)
print("\nColuna removida:")
print(telefone_removido)