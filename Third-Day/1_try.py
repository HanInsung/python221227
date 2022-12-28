#try.py

def divide(a,b):
    return a/b

try:
    # 에러처리
    result  = divide(5,0)
    
except ZeroDivisionError : 
    print("0으로 나누면 안됨!")
except TypeError : 
    print("숫자만 연산가능!")
else:
    print("result-{0}".format(result))
finally:
    print("무조건 실행(이중으로 체크)")

print("=== All Excection End~~")
