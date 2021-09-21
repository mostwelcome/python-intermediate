"""
1 1 0 1 1
1 1 1 1 1
1 1 1 0 1
1 1 1 1 1
0 1 1 1 1


0 0 0 0 0
0 1 0 0 1
0 0 0 0 0
0 1 0 0 0
0 1 0 0 1
0 0 0 0 0
"""

arr = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
]

row_idx = []
col_idx = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            row_idx.append(i)
        if arr[j][i] == 0:
            col_idx.append(i)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i in row_idx or j in col_idx:
            arr[i][j] = 0

print(arr)
