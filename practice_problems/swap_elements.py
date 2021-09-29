def swap_elements(n):
    n[0], n[len(n)-1] = n[len(n)-1], n[0]
    return n


print(swap_elements([1, 2, 3, 4, 5, 6]))
