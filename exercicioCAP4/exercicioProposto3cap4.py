import numpy as np

ds = np.loadtxt(
                'space.csv',
                delimiter=';',
                dtype=str,
                encoding='UTF-8'
                )
#1
print(ds[0, :])

contagemDeMissoes = ds[:, 7]
print(np.unique(contagemDeMissoes, return_counts=True))
totalDeMissoes = np.size(ds[1:, 7])
print('Porcentagem de missoes em sucesso:', (3879/totalDeMissoes)*100, '%')

#2

contagemDeCusto = ds[1:, 6]
print(np.unique(contagemDeCusto, return_counts=True))
semZero = contagemDeCusto[contagemDeCusto.astype(float) > 0] 
print(semZero)
media = np.mean(semZero.astype(float))
print('Media dos custos: ', media) 

#3

nomeUsa = np.size(ds[ds[0:, 1] == 'US Air Force']) 
print('Quantas missoes espaciais os EUA realizaram: ', nomeUsa)

#4
print(ds[0, :])
missao = ds[ds[:, 1] == 'SpaceX']
valorCaro = missao[:, 6]
print(missao)
print('Missao caro: ', valorCaro[23]) 

#5
listaEmpresas = ds[1:, 1]
nomes, contagemMissoes = np.unique(listaEmpresas, return_counts=True)
print(listaEmpresas)
for nome in nomes:
    print('nome: ', nome, ' Quantidade de Missoes: ', contagemMissoes[nome == nomes][0])



