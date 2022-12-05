from driver import Driver
from search import editDriver
# from search import deleteDriver
# from search import allDriver


# from search import searchDriver
# driver = searchDriver("123")
# if len(driver)==0:
#     print("Record not found")
# else:
#     print(driver)


# # 2
# # wee
# # 123
driver2 = Driver(2, 'tee', '009')
result = editDriver(driver2)
print(result)

result = deleteDriver(2)
print(result)

drivers = allDriver()
print(drivers)
