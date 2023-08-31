import numpy as np


#1)
arr = np.linspace(0, 1, 21)
print(arr)
print("______________________________________________________________________________________")
#2) 
arr1 = np.arange(0, 51, 2)
arr2 = np.arange(50, 100, 2)
arr3 = np.concatenate([arr1, arr2])
print(arr3)
print("______________________________________________________________________________________")
#3) 
print(np.flip(np.sort(arr3)))
print("______________________________________________________________________________________")
#4) 
arr4 = np.ones((3, 4))
print(arr4)
arr5 = arr4.reshape(12)
print(arr5)
print("______________________________________________________________________________________")
#5)
arr6 = np.array([[1, 2, 3]
                ,[4, 5, 6]
                ,[3, 3, 3]])
x = len(arr6)  
y = len(arr6[0]) 
mult = x * y
arr7 = arr6.reshape(mult)
if((mult % 2) == 0):
    print("Pode se tornar par!")
    print(arr7)
else:
    print("Pode se tornar impar!")
    print(arr7)