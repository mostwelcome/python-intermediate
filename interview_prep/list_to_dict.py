# Convert two lists into a dict

def convert(l1, l2):
    return dict(zip(l1, l2))


print(convert(['swag', 'tua', 'putul'], [1, 2, 3]))
