import numpy as np

paises = np.loadtxt('paises.csv', 
                    dtype=str, 
                    delimiter=';',
                    encoding='utf8')

print(paises[0:,0:4])