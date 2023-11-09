import numpy as np

paises = np.loadtxt('paises.csv', 
                    dtype=str, 
                    delimiter=';',
                    encoding='utf8')

cond = np.char.equal(paises, "NORTHERN AMERICA")
paises2 = paises[cond]
paises3 = paises2[0: 0]
print(paises2)