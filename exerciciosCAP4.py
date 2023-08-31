import numpy as np

#EXERCICIOS
#1) CRIAR UM VETOR DE 0 A 1 DE TAMANHO 21
arr = np.linspace(0, 1, 21)
print(arr)
print("")
#2) CONCATENAR 1 VETOR DE PARES DE 0 A 51 E OUTRO VETOR DE PARES DE 50 A 100
arr1 = np.arange(0, 51, 2)
arr2 = np.arange(50, 100, 2)
arr3 = np.concatenate([arr1, arr2])
print(arr3)
print("")
#3) ORDENAR O VETOR DA QUESTAO 2 EM DESCRESCENTE
print(np.flip(np.sort(arr3)))
print("")
#4) UMA MATRIZ 3X4 FORMADA POR UNS
arr4 = np.ones((3, 4))
print(arr4)
arr5 = arr4.reshape(12)
print(arr5)
print("")
#5)CRIAR UMA MATRIZ QUALQUER, EXTRAIR NUMERO DE LINHAS E COLUNAS, MULTIPLICAR E DIZER SE É ELA PODE SE TORNAR UM VETOR COM NUMERO PAR OU IMPAR DE ELEMENTOS
arr6 = np.array([[1, 2, 3]
                ,[4, 5, 6]
                ,[3, 3, 3]])
x = len(arr6)  #numero de linhas
y = len(arr6[0]) #numero de colunas
mult = x * y
arr7 = arr6.reshape(mult)
if((mult % 2) == 0):
    print("Pode se tornar par!")
    print(arr7)
else:
    print("Pode se tornar impar!")
    print(arr7)