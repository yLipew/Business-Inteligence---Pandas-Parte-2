import pandas as pd

df = pd.DataFrame({
    'Valores': range(1, 21)
})

# Selecionando da 5ª até a 12ª linha
print(df[4:12])