#web1
#웹에 데이터를 수집
from bs4 import BeautifulSoup

#웹페이지 로딩
page  = open("c:\\work\\Forth-Day\\test01.html","rt",encoding="utf-8").read()

#검색할 객체(xml문서, xml)
soup = BeautifulSoup(page,"html.parser")

#전체를 보기
#print(soup.prettify())

#find_all //list 형 리턴
#문서 내 "p" 테크만 모두 추출
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#조건 <p class=outer-text> //class_ : class가 키워드라 인자명으로 표기
#print( soup.find_all("p", class_='outer-text'))

#내부컨텐츠만 출력

for item in soup.find_all("p"):
    title = item.text.strip().replace("\n","")
    print(title)


