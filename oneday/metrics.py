import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)

arr2 = arr.flatten()
print(arr.dtype)
print(arr.shape)
print(arr2)


m1 = np.matrix('1,2,3; 2,3,4; 2,3,4')
m2 = np.matrix('8,7,9; 7,2,2; 2,3,4')
print('m1: ',m1)
print('m2: ',m2)
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)

