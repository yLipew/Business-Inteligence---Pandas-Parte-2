import pandas as pd

produtos = pd.Series(['Notebook', 'Mouse', 'Teclado'], index=['p1', 'p2', 'p3'])
precos = pd.Series([3500, 80, 150], index=['p1', 'p2', 'p3'])

df = pd.DataFrame({
    'Produto': produtos,
    'Preço': precos
})

print(df)