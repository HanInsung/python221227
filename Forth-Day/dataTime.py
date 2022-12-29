import time

print(time.time())
print(time.gmtime())
print(time.localtime())

print(time.localtime())

now = time.localtime()
print(time.strftime('%Y%m%d', now))
print(time.strftime('%c', now))
print(time.strftime('%x', now))
print(time.strftime('%X', now))
print(time.strftime('%H%M%S', now)) 

# cnt = 0
# while True:
#     time.sleep(1)
#     #cnt += 1
#     print("Time Sleep Test!!! {0}".format(time.time()))


#from datetime import *

# print(dir())

# print(date(2022,1,1))
# print(date(2022,12,29))
# print(now())
# print(date.today())
# print(date(2022,1,1))
from datetime import *
print(datetime.today())
print(datetime.today().year)
d = datetime(2021, 5, 4, 0, 44, 5, 707495)
print(d)
print(datetime(2021, 12, 25))
d = datetime.strptime('20211225', '%Y%m%d')
print(type(d))
print(d)

#파일패스 출력
from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))

#랜덤함수 출력
from random import *
print(random())
print(randrange(1,7))
print(choice([True, False]))

#운영체제 정보
from os import *
print(datetime.today())
print(datetime.today().year)

#from glob import glob
#print(glob(r"C:\U*"))              # C:\에서 이름이 U로 시작하는 디렉터리나 파일을 찾기

#for item in glob.glob("c:\\work\\*\\*.py"):
#    print(item)
