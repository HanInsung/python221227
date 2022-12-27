#class1.py
#1) Class Define
class Person:
    def __init__(self): #create method 
        self.name = "default name"

    def print(self):
        print("My Name is {0}".format(self.name))

#2) Creation Instance copy 
p1 = Person()
p2 = Person()

#3) Call Method
p1.print()
p2.print()
