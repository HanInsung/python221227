f = open("c:\\work\\Forth-Day\\test.txt","wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#fileread

f = open("c:\\work\\Forth-Day\\test.txt","rt",encoding="utf-8")
result = f.read()
print(result)

print("--readlines으로 받기--")
f.seek(0)
lst = f.readlines()

for item in lst:
    #print(item,end="")
    print(item.replace("\n",""))


print("--readline으로 받기--")
f.seek(0)
# print(f.readline().replace("\n",""))
# print(f.readline().replace("\n",""))
# print(f.readline().replace("\n",""))

while data := f.readline() :
    print(data.replace("\n",""))
    

f.close()



