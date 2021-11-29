"""
Increment all the dict values by number 'n'
"""


def increment_dict(d, n):
    d = {key: value + n for (key, value) in d.items()}
    print(d)


d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
increment_dict(d, 5)
