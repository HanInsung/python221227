#demoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---공백문자를 제거---")

u = "<<<  spam and ham  >>>"
result = u.strip("<>")

print(u)
print(result)

result2 = result.replace("spam", "spam egg")
print(result2)

print("분리")

lst = result.split()
print(lst)

print("--다시합치기--")
print( ":)".join(lst))


import re

result = re.search("[0-9]*th","  35th")
print( result)
print(result.group())

# result = re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

#result = re.search("apple","this is apple")
result = re.search("apple","this is Apple".lower())
print(result.group())
result = re.search("\d{4}","올해는 2022년입니다.")
print(result.group())


result = re.search("\d{5}","우리 동제는 52134")

print(result.group())

print("다중라인 ---")
strM = """ 이 문자열은 
다음과 같이 

빈줄도 있습니다. """

#^:시작할때, .:글자 하나, +:하나라도(출현회수)

carot = re.compile("^.+", re.M)
print(carot.findall(strM))


