#demoDict.py

device = {"아이폰":5, "아이패드":10, "윈도우타블렛":15}
print( type(device))

print(device)

device["맥북"]  = 20
print(device)

device["아이폰"] = 6
print(device)

del device["아이폰"]
print(device)

print("--bool--")

print( bool(0))
print( bool(""))
print( bool([]))
print( bool(3))
print( bool("test"))
print( bool([1,2,3]))
isRight = True

print( type(isRight))

print( bool(1<2))
print( bool(1 != 2))
print( True and True and True)
print(True and True and False)
print(True or False or False)

print(5/2)
print(5//2)
print(5%2)

