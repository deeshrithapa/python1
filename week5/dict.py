# collection of key and value
# declare and initialise
# dict1 = {1}
# print(type(dict1)) # set
# dict1 = {}
# print(type(dict1))  # dict

# student = {
#     'sid' : 1,
#     'name' : "dee t",
#     'email' : 'deeshri@gmail.com'
# }
# print(type(student))
# print(student)
# student.clear()
# print(student)

# address = {
#     'house number:' : 12,
#     "street:": 1,
#     'tole:': "ekata tole",
#     'ward no:': 12,
#     'vdc:': "vdc",
#     "district:" : "kathmandu",
#     "zone:" : "bagmati",
#     "state:" : "bagmati"
# }
# print(address)

#copy
# student = {
#     'sid' : 1,
#     'name' : "dee t",
#     'email' : 'deeshri@gmail.com'
# }
# s1 = student.copy()  # copy by value ( only copies value)
# print(id(student))
# print(id(s1))
# s2 = student  # copy by reference (memory copy)
# print(id(s2))

# get
student = {
    'sid' : 1,
    'name' : "dee t",
    'email' : 'deeshri@gmail.com'
}
# print(student.get('sid'))
# print(student['sid'])
# print(student.get('name'))
# print(student.get('email'))
# print(student['name'])
# print(student['email'])
#
# #items
# print(student.items())
#
# # keys function
# print(student.keys())
# # values
# print(student.values())


# keys and for loop
keys = student.keys()
for key in keys:
    print(key, "=", student[key])














