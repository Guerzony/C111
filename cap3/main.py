#EXERCICIOS:
#1)
selecoes = ['Real Madrid','Barcelona','Manchester City','Bayern Munique','Juventus ']
print(selecoes[:3]) #PRINT DOS TRES PRIMEIROS COLOCADOS
print(selecoes[3:]) #PRINT DOS DOIS ULTIMOS COLOCADOS
selecoes.sort()  #ORGANIZANDO ITENS EM ORDEM ALFABETICA
print(selecoes) #PRINT DA LISTA COM ITENS ORDENADOS
print(selecoes.index('Barcelona')) #PRINT POSIÇÃO DO Barcelona NA LISTA

#2)
loja1 = {'Samsung','Apple'}
loja2 = {'Huawei','Xiaomi'}
print('O total de itens da loja 1 é:' , len(loja1))
print('Voce podera comprar na loja 1, celulares das marcas: ', loja1)
print('O total de itens da loja 2 é:' ,len(loja2))
print('Voce podera comprar na loja 2, celulares das marcas: ', loja2)

#3)
numero = int(input('Entre com o numero de alunos: '))
DicAlunos = {} #dicionario de alunos
for i in range(numero):
    aluno = {}
    nome = input('Entre com o nome do aluno:')
    aluno['name'] = nome
    nota = input('Entre com a nota do aluno:')
    aluno['nota'] = nota
    DicAlunos[i] = aluno

for i in range(len(DicAlunos)):
    if DicAlunos[i]['nota'] >= '60':
        DicAlunos[i]['Situacao'] = 'AP'
    else:
        DicAlunos[i]['Situacao'] = 'RP'
print(DicAlunos)
