import pandas as pd

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'Idade': [18, 19, 17, 18, 20]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)