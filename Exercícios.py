'''Ex 1 ou Nível 1'''
import pandas as pd
import numpy as np #IMPORT DO EX 3 ou Nível 3



series_vazia = pd.Series(dtype='float64')

print(f"Tipo de dado padrão: {series_vazia.dtype}")

frutas = ['Maçã', 'Banana', 'Laranja', 'Morango', 'Uva']



'''Ex 2 ou Nível 2'''
series_frutas = pd.Series(frutas)

print(series_frutas)

import numpy as np

valores = np.array([10, 20, 30, 40])
indices = ['A', 'B', 'C', 'D']

series_custom = pd.Series(data=valores, index=indices)

print(series_custom)





'''Ex 3 ou Nível 3'''
valores = np.array([10, 20, 30, 40])
indices = ['A', 'B', 'C', 'D']

series_custom = pd.Series(data=valores, index=indices)

print(series_custom)




'''Ex 4 ou Nível 4'''
dados = {'jan': 100, 'fev': 200}
meses_indice = ['jan', 'fev', 'mar']

series_meses = pd.Series(dados, index=meses_indice)

print(series_meses)




'''Ex 5 ou Nível 5'''
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

'''data: Os dados que vão preencher a tabela'''
'''index: Rótulos para as linhas'''
'''columns: Rótulos para as colunas'''
'''dtype: Força um tipo de dado específico para todo o conjunto.'''
'''copy: Copia os dados de entrada para evitar que alterações no DataFrame afetem a fonte original (o padrão é False).'''