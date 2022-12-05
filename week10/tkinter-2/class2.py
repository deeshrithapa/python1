class Customer():
    def __init__(self, cid = 0, name=0,address=0, email=0, phone=0):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
    def getCID(self):
        return self.cid
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def setCID(self, cid):
        self.cid =cid
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setPhone(self, phone):
        self.phone = phone
    def __str__(self):
        return("{}, {}, {},{},{}". format(self.cid, self.name, self.address, self.email, self.phone))
