import secrets

a = secrets.randbelow(10)
b = secrets.randbits(4)
print(a)
print(b)


myList = list("ABCDEF")
c = secrets.choice(myList)
print(c)