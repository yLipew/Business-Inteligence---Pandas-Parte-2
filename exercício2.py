import pandas as pd

dados = [
    {'Nome': 'Ana', 'Cargo': 'Analista'},
    {'Nome': 'Bruno', 'Cargo': 'Gerente', 'Bonus': 500}
]

df = pd.DataFrame(dados)

print(df)

'''A coluna 'Bonus' ficará com valor NaN para Ana, pois ela não possui esse campo no dicionário original.'''