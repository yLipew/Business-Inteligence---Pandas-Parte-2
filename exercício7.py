import pandas as pd

df = pd.DataFrame({
    'Modelo': ['Carro1', 'Carro2', 'Carro3', 'Carro4', 'Carro5', 'Carro6'],
    'Preço': [20000, 25000, 30000, 35000, 40000, 45000]
})

# Selecionando 4º e 5º carros (índices 3 e 4)
print(df.iloc[3:5])