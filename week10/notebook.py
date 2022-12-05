class Notebook():
    def __init__(self, nid = 0, page= 0, price=0):
        self.nid = nid
        self.page = page
        self.price = price
    def getNID(self):
        return self.nid
    def getPage(self):
        return self.page
    def getPrice(self):
        return self.price
    def setNID(self, nid):
        self.nid =nid
    def setPage(self, page):
        self.page = page
    def setPrice(self, price):
        self.price = price
    def __str__(self):
        return("{}, {}, {}". format(self.nid, self.page, self.price))


