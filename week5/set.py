from array import array
# set is a collection of unique values
# print(help(set)) - {}
# # declare and initialise
# set1 = {}
# set1 = set([1, 2, 3, 4])  # list to set
# set1 = set((1, 2, 3, 4))  # tuple to set
# set1 = set(array('i', [1, 2, 3, 4, 5]))  # array to set

# add
# set1 = {1, 2, 3}
# set1.add(6)
# set1.add(1)
# print(set1)

#clear
# set1 = {1, 2, 3, 4, 5}
# print(set1)
# set1.clear()
# print(set1)

# copy()
# set1 = {1, 2, 3, 4}
# set2 = set1
# print(id(set1))  # same
# print(id(set2))  # same (copy by reference)
# set3 = set1.copy()
# print(id(set3))  # different (copy by value)

# # difference
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 4, 3}
# set3 = set1.difference(set2)
# print(set3)
# set3 = set2.difference(set1)
# print(set3)

# intersection
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.intersection(set2)
# print(set3)  # common

# union
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.union(set2)
# print(set3)

# pop
# remove
# set1 = {1, 2, 3, 4, 5, 1, 2, 3}  # doesn't show repetitive values
# print(set1)
# set1.pop()  # remove from -1 index
# print(set1)
# set1.remove(3)  # removes value
# print(set1)












