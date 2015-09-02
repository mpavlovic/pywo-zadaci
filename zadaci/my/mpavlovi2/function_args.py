__author__ = 'Milan'

def func(m, n = 1):
    return m+n

def func2(arg1, arg2, defarg1=1, defarg2=2, *args): # prima varijabilni broj argumenata (zadnjeg parametra)
    pass

def sumargs(*args):
    sum = 0
    for item in args:
        sum = sum + item
    return sum

# Keyword arguments
def func3(*args, **kwargs):
    # args je lista argumenata
    # kwargs je dictionary
    print("args: " , args)
    print("kwargs: " , kwargs)

#func3(1, 2, 3, debug=True)

myTuple = (1,2,3,4)
#print(sumargs(*myTuple))

myDict = {'debug': False, 'verbose': True}

func3(myDict)
func3(*myDict)
func3(*myTuple, **myDict)

list = range(1,10)
a, b, *c = list # u c je ostatak liste bez prva dva elementa
first, *_, last = list

#Zadaca - Horner
