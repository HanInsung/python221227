print("Hello World")

strA = "pyton is strong language!"
x=100
pi = 3.14

print(strA)
print(strA[0])
print(strA[1])
print(strA[:3])
print(strA[:-2])
print(strA[-2:])

strB = """다중라인
으로 엔터 키 저정 
테스트"""

print(strB)

print("하나\t 둘 \t 셋")

colors = []
colors.append("White")
colors.insert(1,"Red")
colors += "Blue"

print (colors)

colors.pop()
colors.pop()

colors += ["Blue"]

print(colors)

count = colors.count("Blue")

for i in range(count):
    colors.remove("Blue")

print("--------Result-------")
print(colors)

#set

setA = {1,2,3,4}
setB = {2,3,3,4}

print(setA)
print(setB)
print(setA.union(setB))
print(setA.intersection(setB))


print("--Tuple--")
args = (2,3)

def times(a,b):
    return a+b, a*b

print(times(*args))

result = times(3,4)
print("---형식변화---")

a = set((1,2,3))
print(type(a))

b = list(a)
b.append(4)
print( type(b))
print(b)
