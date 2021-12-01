test_cases = int(input())
while test_cases != 0:
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split()))
    index = n - (k % n)
    for i in range(index, n):
        print(a[i], end=' ')
    for i in range(index):
        print(a[i], end=' ')

    test_cases -= 1
