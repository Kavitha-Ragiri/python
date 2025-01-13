import random

c=random.random()
print(c)

a=random.randint(1,10)
print(a)

b=random.randrange(1,5)
print(b)

li=[12, 3, 4, 56, 6, 345, 34, 67, 888]
random.choices(li)
print(li)