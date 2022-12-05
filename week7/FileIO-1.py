# create new file

# file = open("data.txt","w")
# file.write("hello!\n")
# file.write("how are you?\n")
# file.close()

# append on file (add on last)
# file = open("data.txt","a")
# file.write("good\n")
# file.close()

# read file
file= open("data.txt","r")
contents = file.readlines()
print(contents)