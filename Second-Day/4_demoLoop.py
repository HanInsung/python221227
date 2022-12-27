#demoLoop.py

# score = int(input("input Score:"))

# if 90 <= score <=100 :
#     grade = "A"
# elif 80 <= score <90 :
#     grade = "B"
# elif 70 <= score <80 :
#     grade = "C"
# else : 
#     grade = "D"

# print("GRADE : ", grade)

val = 5
while val > 0 :
    print(val)
    val -= 1
d = {"apple":100, "orange":200, "banana":300}
for item in d.items():
    print(item)
    
lst = [0,1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break
    print("item:{0}", format(i))

for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}", format(i))

print("---수열함수--")
print(list(range(10)))
print(list(range(2000,2023)))
print(list(range(1,32)))

print("-----리스튼 내장-----")

lst = list(range(10))
print([i**2 for i in lst if i>5])

d = {100:"apple", 200:"banana",300:"kiwi"}
print([v.upper() for v in d.values()])

print("---필터링---")
lst = [10,25,30]

iterL = filter(None,lst)
for item in iterL:
    print(item)

def getBiigerThan20(i):
    return i>20

print("---필터링 함수---")
iterL = filter(getBiigerThan20,lst)
for item in iterL:
    print(item)

print("---필터링 lambda 함수(중요~~~~~) ---")
iterL = filter(lambda x:x>20 ,lst)
for item in iterL:
    print(item)


iterR = filter(lambda x:x+2,lst)
print([item for item in iterR])