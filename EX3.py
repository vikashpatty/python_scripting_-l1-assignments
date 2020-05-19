# Exercise – 3: Filename: ex3.py
# Implement the function isListOfInts(), which takes a list, and checks if the list has
# only "int" type values, as per the specification given below:
# • The function should return True, if the list has only "int" type values, otherwise
# should return False.
# • The function should return True, if an empty list is passed as argument.
# • If the argument is not of ‘list’ type, then the function should throw ValueError
# exception, with the error message 'arg not of <list> type'
# • The function should have only one return statement.
# To test correctness of the function isListOfInts(),implement the function testList()
# which is called as shown below and should produce output as indicated.
# Function call Expected output
# testList([])
# testList([1])
# testList([1,2])
# testList([0])
# testList(['1'])
# testList([1,'a'])
# testList(['a',1])
# testList([1, 1.])
# testList([1., 1.])
# testList((1,2))
# [] --> True
# [1] --> True
# [1, 2] --> True
# [0] --> True
# ['1'] --> False
# [1, 'a'] --> False
# ['a', 1] --> False
# [1, 1.0] --> False
# [1.0, 1.0] --> False
# ValueError: (1, 2) - arg not of <list> type


def isListOfInts(l):
    if type(l) is not list:
        raise ValueError("{0} - arg not of <list> type".format(l))
    flag  = True
    for i in l:
        if type(i) is int:
            continue
        else:
            flag = False
    return flag

def testList():
    print(isListOfInts([]))
    print(isListOfInts([1]))
    print(isListOfInts([1,2]))
    print(isListOfInts([0]))
    print(isListOfInts(['1']))
    print(isListOfInts([1,'a']))
    print(isListOfInts(['a',1]))
    print(isListOfInts([1, 1.]))
    print(isListOfInts([1., 1.]))
    print(isListOfInts((1,2)))
testList()
