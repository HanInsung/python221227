dataA = 1.2
print(id(dataA))
dataA = 2
print(id(dataA))


def CallbyRefTest(valA):
    valA[0] = "H"
    return valA

valA = ["J","A","M"]
print(valA)
print(id(dataA))

valB = CallbyRefTest(valA)

print(valB)
print(id(valB))

def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("함수내부",x1)

wordlist = ["J","A","M"]
change(wordlist)
print("호출후:",wordlist)


import copy

lst = [100,200,300]

lst2 = copy.deepcopy(lst)
lst2[0] = 101

print(lst)
print(lst2)
print(id(lst),id(lst2))

#함수내부의 이름 해석 순서(Local, Global, Build-in: LLGB)
x = 5
def func(a):
    return x+a

#호출
print(func(1))

def func2(a):
    x = 10
    return x+a
#호출
print(func2(1))


