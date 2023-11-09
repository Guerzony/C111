import numpy as np

paises = np.loadtxt('paises.csv', 
                    dtype=str, 
                    delimiter=';',
                    encoding='utf8')

regioes = paises[0:,1]
paises2 = paises[regioes == 'LATIN AMER. & CARIB']
pais_maior_gdp = paises2[max(paises2[1:,8])]
print(max(paises2[1:,8]))