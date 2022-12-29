#web2
import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

soup = BeautifulSoup(data,"html.parser")

cartoons = soup.find_all("td",class_="title")
print("개수:{0}".format(len(cartoons)))

import re

#carot = re.compile("^.+", re.M)

for item in cartoons:
    title = item.find("a").text
    link = item.find("a")["href"]
    title_item = title.split("<")
    title_item = title_item[1][:-1]
    print(title_item)
    
    #print(link)
 
    
    #print(carot.findall(title))

#<td class="title">
# <a href="/webtoon/detail">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
#</td>