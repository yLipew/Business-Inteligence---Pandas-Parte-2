import pandas as pd

df = pd.DataFrame({
    'População': [213, 45, 19]
}, index=['Brasil', 'Argentina', 'Chile'])

# Selecionando dados do Brasil
print(df.loc['Brasil'])