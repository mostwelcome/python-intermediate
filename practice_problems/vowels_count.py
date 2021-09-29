VOWELS_LIST = list('AEIOUaeiou')


def count_vowels(n):
    count = 0
    for i in n:
        if i in VOWELS_LIST:
            count += 1

    print(f'No of vowels: {count}')


count_vowels('swagata')
