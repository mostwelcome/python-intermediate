def find(check_here):
    even_list = [i for i in check_here if i % 2 == 0]
    odd_list = [i for i in check_here if i % 2 != 0]
    return len(even_list), len(odd_list)


check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = find(check)

print(f'No of odd elements : {odd} \nNo of even elements : {even}')
