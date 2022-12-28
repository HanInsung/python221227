#Global Variable
str = "Not Class Member"
#Class Define

class GString:
    def __init__(self):
        #instance memeber variable
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):

        #파이썬은 모호한 것 보다는 명확한 것이 좋다~
        print(self.str)
#Creation instance
g = GString()
#Call Method
g.set("First Message")
g.print()
