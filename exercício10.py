import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Salário': [3000, 4000, 5000]
})

# 1. Transposta
print("Transposta:")
print(df.T)

# 2. Tipos de dados
print("\nDtypes:")
print(df.dtypes)

# 3. Total de elementos
print("\nSize:")
print(df.size)

# 4. Últimas duas linhas
print("\nTail:")
print(df.tail(2))