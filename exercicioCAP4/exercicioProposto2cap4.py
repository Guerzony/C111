import numpy as np

#1)
np.random.seed(5)
arr = np.random.uniform(-1, 1, 10) 
arrayMultiplicado = arr*100
arrayInteiro = arrayMultiplicado.round() 
print(arr)
print('primeiro array multiplicada por 100 com numero inteiro', arrayInteiro)

#2)
np.random.seed(10)
arr2 = np.random.randint(1, 50, 16).reshape(4, 4)
print('Array 4x4: ', arr2)

#3)
print('Media das colunas: ', arr2.mean(axis=0))
print('Media das linhas: ', arr2.mean(axis=1))

#4)
print('Numero / quantidade que aparece:', np.unique(arr2, return_counts=True))
unique = np.unique(arr2, return_counts=True)[0] 
counts = np.unique(arr2, return_counts=True)[1] 
numeros = unique[counts == 2] 
print('Numeros que aparecem 2 vezes: ', numeros)