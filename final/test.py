from customerinfo import customer
from customer import saveCustomer
sfrom driverinfo import Driver
from drivers import saveDriver

# Test-1
# cid = name = address = email = phonenumber = None
# cid = int(input("Enter ID : "))
# name = input("NAME : ")
# address = input("ADDRESS : ")
# email = input("EMAIL : ")
# phonenumber= input("PHONE NUMBER : ")
# save = customer(cid, name, address, email, phonenumber)
# saveCustomer(save)

#testdriver -1
did = name = address = email = phone_number = license_plate = None
did = int(input("ENTER ID: "))
name = input("ENTER NAME: ")
address = input("ENTER ADDRESS: ")
email = input("ENTER EMAIL: ")
phone_number = input("ENTER PHONE NUMBER : ")
license_plate = input("ENTER LICENSE PLATE: ")
d1 = Driver(did, name, address, email, phone_number, license_plate)
saveDriver(d1)