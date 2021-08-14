from numpy import *

arr = array([1, 2, 3, 4])
arr2 = array([5, 6, 7, 8, 9])
# arr += 5

print(concatenate([arr, arr2]))

arr3 = arr2

print(arr2, 'id : ', id(arr2))
print(arr3, 'id : ', id(arr3))

arr4 = arr2.view()
arr5 = arr2.copy()
print(arr4, 'id : ', id(arr4))
print(arr5, 'id : ', id(arr5))
arr2[1] = 50

print(arr4)
print(arr5)
