#DemoForm.py
#DemoFormui(화면단) + DemoForm.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import urllib.request
from bs4 import BeautifulSoup

#변경
form_class = uic.loadUiType(".\\Fifth-Day\\DemoForm2.ui")[0]

#폼 클래스(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")

    def firstClick(self):
        f_handle = open("webtoon.txt","wt", encoding="utf-8")

        for i in range(1,6):
            url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
            #print(url)

            data = urllib.request.urlopen(url)

            soup = BeautifulSoup(data,"html.parser")

            cartoons = soup.find_all("td",class_="title")
            #print("개수:{0}".format(len(cartoons)))
            #carot = re.compile("^.+", re.M)
            
            for item in cartoons:
                title = item.find("a").text
                link = item.find("a")["href"]
                title_item = title.split("<")
                title_item = title_item[1][:-1]
                #m = re.search('<(.*?)>', title_item)
                #print (m.group(1))

                print (title_item)
                f_handle.write(title + "\n")

                #print(link)

        f_handle.close()
            
    
    def secondClick(self):
        self.label.setText("두번째 버튼")

    def thirdClick(self):
        self.label.setText("세번째 버튼")

#진입점을 체크
if __name__ == "__main__":
    #실행 프로세스를 생성(Excel.exe)    
    app = QApplication(sys.argv)
    
    #폼클래스 생성
    demoWindow = DemoForm()
    
    #화면에 출력
    demoWindow.show()

    #이벤트 처리 대기(실행중)
    app.exec_()
