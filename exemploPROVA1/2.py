import numpy as np

paises = np.loadtxt('paises.csv', 
                    dtype=str, 
                    delimiter=';',
                    encoding='utf8')

regioes = np.unique(paises[1:,1])
print(regioes)
print('contagem de regiões = ', np.count_nonzero(regioes))