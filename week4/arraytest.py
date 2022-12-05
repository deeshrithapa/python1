from array import array
# arr1= array('i', [])
# arr1.append(6)
# arr1.append(7)
# arr1.append(8)
# print(arr1)

# reading 25 ages
# ages = array('i', [])
# MAX = 5
# for i in range (MAX):
#     tmp= int(input("enter age:"))
#     ages.append(tmp)
# print(ages)

# count() # search value
# arr1= array('i', [1,2,2,3,3,4,5,6])
# result = arr1.count(1)  # output= 1 bc there is only 1 once in the list
# print(result)
# result1 = arr1.count(3)  # output = 2
# print(result1)
# tmp = int(input("enter no to search :"))
# result = arr1.count(tmp)
# print("found {} times".format(result))



# index # can onlu return one value and cannot return multiple values
# arr1= array('i', [1,2,2,3,3,4,5,6])
# tmp = 5
# count_result = arr1.count(tmp)
# # indexing
# arr1= array('i', [1,2,2,3,3,4,5,6])
# result_count = arr1.count(9)
# if result_count >= 1:
#     result = arr1.index(9)
#     print(result)
# else:
#     print("not found")
# result = arr1.index(4)  # inside() is value and out is 5 bc the counting starts from 0
# print(result)

#  print(help(array))

# num = array('i',[1,2,3,4,4,4])
# result = num.count(5)
# print(result)  # result= 0
# try:
#     result1 = num.index(4)  # value
#     print(result1)  # value error
# except:
#     print("not found")

# insert (self,i,v,/)  #add new elements , shift to right
# nums = array('i', [3, 4, 7, 5, 1])
#  nums.insert(2, 9)
# nums.insert(7,9) # it goes to the end
# print(nums)

# pop (self, i== -1,/)  # remove index
# nums = array('i',[3, 5, 7,5,1])
# nums.pop()  # removes the element in -1 index
# print(nums)
# nums.pop(i==2) #error
# print(nums)

# remove (self, v,/)
# try:
#     nums = array('i',[3, 5, 7, 5, 1])  # removes value
#     nums.remove(50)
#     print(nums)
# except:
#     print("not found")

# reverse (self, v,/)
# try:
#     nums = array('i', [3, 5, 6, 2, 1])
#     print(nums)  # prints in the normal order
#     nums.reverse()
#     print(nums)  # prints in the reverse order
# except:
#     print("error")

# sorting array elements- ASC/DESC (ascending/descending)









