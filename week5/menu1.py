import sys
list1 = []  # blank list
while(True):
    print("---main menu---")
    print("1. ADD")
    print("2. Display All")
    print("0. Exit")
    print("---------------")
    choice = int(input("enter your choice:"))
    print("---------------")
    print("your choice is :{}".format(choice))
    if(choice>=0 and choice<=2):
        match choice:
            case 1:
                tmp = int(input("enter any number:"))
                list1.append(tmp)
            case 2:
                print(list1)
            case 0:
                print("bye!")
                sys.exit()

