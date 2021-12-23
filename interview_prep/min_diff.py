def min_diff(arr):
    arr = sorted(arr)
    length = len(arr)
    diff = float('inf')

    for i in range(length - 1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]

    return diff


arr = [5, 32, 45, 10, 3]
print(f'Minimum difference in two numbers is :{min_diff(arr)}')
