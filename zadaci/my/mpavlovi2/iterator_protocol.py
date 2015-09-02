__author__ = 'Milan'

list = [1, 2, 3]
for x in list:
    print(x)

string = "123"
for char in string:
    print(char)

mySet = set(list)

for element in mySet:
    print(element)

dict = {'a': 1, 'b': 2}

for key in dict:
    print(key)

# pazi
for key, value in dict.items():
    print(key, value)

# pazi
l = [1, 6, 9, 8, 25]
for i, x in enumerate(l):
    print(i, x)

print("---------------Generators---------------")

r = range(1, 50)
kv_gen = (x ** 2 for x in r if x ** 2 < 200)
for x in kv_gen:
    print(x)


# generatori u vise linija
def gen1():
    r = range(1, 50)
    for x in r:
        yield x**2

g = gen1()
for x in g:
    print(x)

def genZeroOne():
    while(True):
        yield 0
        yield 1

#for x in genZeroOne():
 #   print(x)

#Zadatak - Fibonaccijev niz 0,1,1,2,3,5,8...
def fibonacciGen(limit = 20):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

print([x for x in fibonacciGen(100)])



