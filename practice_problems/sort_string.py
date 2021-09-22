def sort_string(st):
    return ' '.join(sorted(list(st.split(" ")), key=str.casefold))


print(sort_string('banana ORANGE apple'))
