# 1. create a blank list
import random

list= []
print(list)

# append 100 random numbers in list (int)
MAX = 100
for i in range(MAX):
    tmp = random.randint(16, 24)
    list.append(tmp)
print(list)

# export all values to data.txt file (save)
# file1 = open("data.txt", "w")
# for i in range(len(list)):
#     file1.writelines(str(list[i]))
# file1.close()

# print max number of list
max = max(list)
print(max)
print(min(list))

# search user given number in a list
num = int(input("enter any number to search:"))
result = list.count(num)
if (result==0):
    print("not found")
else:
    print("found{} times".format(result))

# calculate average age
# sorting ages in ASC order
# sorting ages in DESC order






