# def readint():  # read input from keyboard
#     tmp = input("enter any number:")
#     tmp = int(tmp)  # convert into integer
#     return tmp  # return value of tmp
# def calcsum(n1, n2):  # to calculate sum
#     return n1 + n2
# def printmesssage(lable, value):
#     print(lable, value)

def f1():  # no parameter, no return
    print("hello from f1")
def f2():  # no parameter, return type
    return "hello fom f2"
def f3(message):  # parameterised, no return
    print(message)
def f4(n1, n2):  # parameterised, return type
    return n1 + n2
def f5():   # nested call
    f4(2,7)
    f3(tmp)
def f6(n1=0, n2=0): #
    return (n1=n2)

