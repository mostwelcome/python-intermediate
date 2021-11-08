import random

a = random.randint(1, 10)
b = random.randrange(1, 100, 10)

print(a)
print(b)

myList = list("ABCDEFGH")

print(myList)

random.shuffle(myList)
print(myList)

print(random.choice(myList))
