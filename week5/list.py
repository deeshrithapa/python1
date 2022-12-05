# print(help(list))
# declare and initialise
# list1 = [5, 6, 7, 1, 2]  # style 1
# list1 = list(5, 6, 7, 8, 9)  # style 2
# arr1 = array('i', [7, 8, 9, 2, 3])  # array declare and initialise
# list1= list(arr1) # array to list #style 3

# indexing and slicing
# indexing
# list1 = list([5, 6, 7, 8, 9])  # 0 - 4
# try:
#     print(list1[0])
#     #print(list1[10])  # index error
#     print(list1[4])
#     print(list1[-5])
#     print(list1[-10])  # index error
# except:
#     print("error")


# slicing
# extracting multiple values
# list1 = list([5, 6, 7, 8, 9, 3, 4, 2, 4, 7])  # 0 to 9
# result = list1[8]
# print(result)  # output = 4
# result1 = list1[5:10]  # includes 5 but not 10
# print(result1)


# list functions:
# append (self, object, /)
# list1 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 9])
# list1.append(True)
# list1.append(False)
# list1.append("hello")
# print(list1)
# clear (self,/)
# list1.clear()
# print(list1)  # output: []
# clear (self, /)
# list1 = [2, 4, 5]  # declare and initialise
# list2 = list1  # list1 assign to list2 -> copy by reference
# list2.clear()  # clear list2
# print(list1)  # print list1
# print(list2)  # print list2
# print (id(list1))  # memory address
# print(id(list2))  # memory address

# copy (self, /)
# list1= [4, 5, 6]
# list2 = list1  # copy by reference -> address
# list3 = list1.copy()  # copy by value
# print(id(list3))
# print(id(list2))
# print(id(list1))

# count (self, value,/)
# list1 = [6, 7, 7, 8, 9, 0, 1, 3, 4]
# num1 = 7
# result = list1.count(num1)
# print(result)

# extend (self, iterable ,/)
# list1 = [6, 7]
# list2 = [3, 4, 5]
# list1.extend(list2)
# print(list1)
# from array import array
# arr1 = array('i',[4,6,7,8,8])
# list1.extend(arr1)
# print(list1)

# index (self, value, start=0, stop= 09989)
# try:
#     list1 = [4, 5, 7, 8, 8]
#     value = int(input("enter any number:"))
#     result = list1.index(value)
#     print(result)
# except:
#     print("not found")


# list1 = [5, 2, 7, 5, 5]
# value = 5
# count = list1.count(value)
# start = -1
# for i in range(count):
#     start += 1
#     print(list1.index(value, start))


# insert (self,index, object,/) it is usually used when list has some elements
# append (self, object, /) it is usually used when list is blank
# list1 = []
# list2 = [5, 2]
# list1.append(5)
# list1.append(6)
# list2.insert(0, 8)
# print(list1)
# print(list2)

# pop (self, index= -1, /) # simply to remove from -1 index
# list1 = [2, 3, 5, 6]
# print(list1)
# list1.pop()
# print(list1)

# # remove (self, value, /) # removes values and not index
# list1 =[3, 4, 5, 6, 5]
# print(list1)
# list1.remove(5)
# print(list1)

# list1 =[3, 4, 5, 4, 5]
# print(list1)
# count = list1.count(5)
# for i in range(count):
#     list1.remove(5)
# print(list1)

# reverse (self, /)
# list1 = [4,5,1,2,9]
# print(list1)
# list1.reverse()
# print(list1)

# sort (self, /, *, key= none, reverse= False)  # ASC
# list1 = [9, 1, 5, 2, 7]
# print(list1)
# list1.sort()  # ascending
# print(list1)
# list1.sort(reverse=True)  # descending
# print(list1)
# list1.sort(reverse=False)  # ascending
# print(list1)












