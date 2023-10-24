import numpy as np

paises = np.loadtxt('paises.csv', 
                    dtype=str, 
                    delimiter=';',
                    encoding='utf8')

literacy = paises[1:, 9]
print('taxa de alfabetização = ', literacy.mean(axis=0, dtype=float), '%')