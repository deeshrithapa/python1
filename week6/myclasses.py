class C1():
   def __init__(self):  # 'self' represents the current class
       self.n1 = None
   def setN1(self, n1):
        self.n1 = n1
   def getN1(self):
        return  self.n1

   def setN2(self, n2):
       self.n2 = n2

   def getN2(self):
       return self.n2


"""
class Person():
    def __init__(self):
        self.pid = None
        self.name = None
        self.address = None

class C2():
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None
"""

class Student():
    def __init__(self):
        self.sid = None
        self.name = None
        self.sub1 = None
        self.sub2 = None
        self.sub3 = None


    def setSID(self, sid):
        self.sid = sid
    def getSID(self):
        return self.sid

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setSub1(self, sub1):
        self.sub1 = sub1
    def getSub1(self):
        return self.sub1

    def setSub2(self,sub2):
        self.sub2 = sub2
    def getSub2(self,sub2):
        return self.sub2

    def setSub3(self,sub3):
        self.sub3 = sub3
    def getSub3(self,sub3):
        return self.sub3










