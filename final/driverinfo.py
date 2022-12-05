class Driver():
    def __init__(self, did= 0, name= None, address= None, email = None, phone_number= None, license_plate= None):
        self.did = did
        self.name =name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.license_plate = license_plate

        def getDID(self):
            return self.did
        def getName(self):
            return self.did
        def getAddress(self):
            return self.address
        def getEmail(self):
            return self.email
        def getPhone_number(self):
            return self.phone_number
        def getLicense_plate(self):
            return self.license_plate

        def setDid(self, did):
            self.did = did
            def setName(self, name):
                self.name = name
                def setAddress(self, address):
                    self.address = address
                    def setEmail(self, email):
                        self.email = email
                        def setPhone_number(self, phone_number):
                            self.phone_number = phone_number
                            def setLicense_plate(self, license_plate):
                                self.license_plate = license_plate

                                def __str__(self):
                                    return ("{}, {}, {}, {},{},{},".format(self.did, self.name, self.address, self.email, self.phone_number, self.license_plate))