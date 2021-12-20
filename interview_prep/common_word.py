# Count the frequency of words appearing in a string
SAMPLE_STRING = 'Tua loves eating apple and mango . Her sister also loves eating apple and mango'


def count_word_frequency(s):
    d = {}
    words = SAMPLE_STRING.split(' ')
    for i in words:
        d[i] = d.get(i, 0) + 1
    return d


print(count_word_frequency(SAMPLE_STRING))
