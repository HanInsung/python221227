def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("ycampus.com", "80"))
print(connectURI(port="80",server="ycampus.com"))

#가변인자(*는 Tuple로 넘기는 경우)
def union(*arg):
    result  = []
    for item in arg:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#lambda Function
g = lambda x,y : x*y
print(g(3,4))
print(g(5,6))
print((lambda x: x*x)(3))
print(globals())
