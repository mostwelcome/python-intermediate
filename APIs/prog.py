def solution(arr):
    print('here')
    sum_dict = {}
    final_list = []
    for i in arr:
        nsub = getSum(i)
        if len(sum_dict) == 0:
            sum_dict[i] = nsub
        if i in sum_dict.keys():
            values = sum_dict[i]
            values += i
            final_list.append(values)
        else:
            sum_dict[i] = nsub

    return max(final_list)


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


a = [51, 71, 17, 42]
print(solution(a))
