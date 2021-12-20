# Find out common letters between two string

def find_common_letter(a, b):
    no = len(set(a.lower()).intersection(set(b.lower())))
    return set(a.lower()) & set(b.lower())


print(find_common_letter('swagata', 'krish'))
