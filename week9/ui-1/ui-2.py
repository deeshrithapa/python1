import sys


def customerManager():
    while (True):

        print("------Customer Management-----")
        print("1. New Customer")
        print("2. All Customers")
        print("3. Search Customers")
        print("4. Edit Customers")
        print("5. Delete Customers")
        print("0. Exit")
        print("--------------------------")
        choice2 = int(input("Enter your choice:"))
        if choice2 == 1:
            print("New Customers")
        elif choice2 == 2:
            print("All Customers")
        elif choice2 == 3:
            print("Search Customers")
        elif choice2 == 4:
            print("Edit Customers")
        elif choice2 == 5:
            print("Delete Customers")
        elif choice2 == 0:
            break
        else:
            print("Out of range")
while(True):

    print("-----Main Menu-----")
    print("1. Customer")
    print("2. Driver")
    print("3. Trip")
    print("0. Exit")
    print("------------------")
    choice1 = int(input("enter your choice: "))
    print("--------------")
    if choice1 == 0:
        print("Bye!")
        sys.exit()

    elif choice1==1:
        customerManager()
    elif choice1==2:
        print("Driver Management")
    elif choice1==3:
        print("Trip Management")
    else:
        print("Out of range")












