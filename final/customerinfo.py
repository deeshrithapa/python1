class customer():
    def __init__(self, cid = None, name = None, address = None, email= None, phonenumber= None):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.phonenumber = phonenumber

        def getCid(self):
            return self.cid
        def getName(self):
            return  self.name
        def getAddress(self):
            return self.address
        def getEmail(self):
            return self.email
        def getPhonenumber(self):
            return self.phonenumber

        def setCid(self, cid):
            self.cid =cid
            def setName(self, name):
                self.name = name
                def setAddress(self, address):
                    self.address = address
                    def setEmail(self, email):
                        self.email = email
                        def setPhonenumber(self, phonenumber):
                            self.phonenumber = phonenumber