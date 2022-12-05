# string class
# collection of characters
# character - symbol of language
# english characters- 256
# alphabets (Aa-Zz) - string
# digits (0-9) - numeric type
# symbols (*,!) - operator
# control (strl,  shift,  alt)
# character- numeric value
# character - ASCII value
# ASCII value - character
# 65 - A
# 66 - B
# declare and initialise
# str1 = "PCPS college"
# str2 = 'PCPS college'
# str3 = """"PCPS college"""  # multi-line string
# str4 = '''PCPS college'''  # multi-line string

# explore str class
# __word__() magic method which are automatically called

# capitalise (self,/)
# Return a capitalised version of the string.
# str1 ="pcps colleg"
# str2 = str1.capitalize()  # convert all characters to lower and then the first one to upper case
# print(str1)
# print(str2)

# casefold (self,/)
# return a version of the string suitable for case-less comparisons.
# password1 = "admin"
# password2 = "admiN"
# result = password1 == password2
# print(result)
# pwd1 = password1.casefold()  # convert into lower case
# pwd2 = password2.casefold()
# result2 = pwd1 == pwd2
# print(result2)

# center (self,  width,  fillchar='',  /)
amount = 123.456
# result = str(amount).center(20, '*')
# result = str(amount).rjust(20, '*')
# result = str(amount).ljust(20, '*')
# print(result)

# count (sub[, start[, end]] -> int
# str1 = """Padding is done using the specified fill character (default is a space)."""
# str2 = "is"
# result = str1.count(str2)
# print(result)

# # reading txt file
# file = open("TheHungerGames.txt")
# # str1 = file.read(100)
# str1 = file.readlines()
# str2 = " ".join(str1)  # converting into string from list
# print(type(str2))
# result = str2.count('she')
# print(result)


# list to string
# list1 = [ 'word1', 'word2', 'word3']
# str2 = " ".join(list1)
# print(str2)

# endswith (suffix[, start[, end]], ) - bool
# str1 = "pcpcs college"
# result = str1.endswith('.')
# print(result)

# expandtabs (self, /, tabsize= 8)
# str1 = "Sn\tName\tAddress"
# str2 = str1.expandtabs(tabsize=20)
# print(str1)

# find (sub[, start[, end]]) - int
# str1 = "pcps college, lalitpur"
# str2 = 'l'
# result = str1.find(str2)
# print(result)
# count =str1.count(str2)
# print(count)
# # manual
# r1 = str1.find(str2)
# print(r1)
# r2 = str1.find(str2, r1+1)
# print(r2)
# r3 = str1.find(str2, r2+1)
# print(r3)
# r4 = str1.find(str2, r3+1)
# print(r4)

# automated
str1 = "pcps college, lalitpur"
str2 = 'l'
count = str1.count(str2)
result = -1
results = []
for i in range(count):
    result = str1.find(str2, result+1)
    results.append(result)
print(results)











