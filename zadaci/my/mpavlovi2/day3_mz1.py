__author__ = 'Milan'

def listToString(list):
    string = ""
    i = 0
    for item in list:
        if i > 0:
            string = string + ", "
        i = i + 1
        string = string + str(item)
    return string # ili samo ", ".join(str(i) for i in r)


def stringToList(string):
    list = []
    for line in string:
        for char in line:
            list.append(char)
    return list # ili samo [str(i) for i in r]

def breakString(string):
    charList = list(string)
    return ",".join(charList)

l = list(range(1, 51))
s = listToString(l)
print(breakString("123"))
