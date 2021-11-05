''' is a container that stores element as dict key, and count as values'''
from collections import Counter

a = 'aaaaaabbbbccc'
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(1))