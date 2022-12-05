# loop design
# 1. start
# 2. stop
# 3. condition
# 4. statements
# 5. modifier
# print 1 to 10
# start=1
# stop =10
# condition = start<=stop
# statements = print(start)
# modifier = start+=1

# start = 1
# stop = 10
# while(start<=stop):
#     print(start, end='')
#     start+=1


# start = 1
# stop = 10
# while(start <= stop):
#     print(start,end=',') # end = horizontal result and not line break
#     start += 1

# print 10 to 1
# design
# start = 10
# stop =1
# condition = start<=stop
# statement = print(start)
# modifier = start-=1
# start=10
# stop=1
# while(start>=stop):
#     print(start, end=',')
#     start -= 1

# print sum of 1 to 10
# start = 1
# stop = 10
# sum= 0
# while(start<=stop):
#     sum+=start
#     start+=1
#     print(sum)
# #print sum of 10 to 1
# start = 10
# stop = 1
# sum =0
# while(start>=stop):
#     sum+=start
#     start-=1
#     print(sum)

# odd number
# num1 = 0
# result = num1%2 #remainder
# if result == 0:
#     print("even")
# else:
#     print("odd")

# print odd numbers of 1 to 10
# start = 1
# stop = 10
# while(start<=stop):
#     if start%2==1:
#         print(start, end=',')
#     start+=1

# print even numbers of 1 to 10
# start = 1
# stop = 10
# while(start<=stop):
#     if start%2==0:
#         print(start, end=',')
#     start+=1

# task
# num = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# sum = 0
# while(num<=num2):
#     sum += num
#     num += 1
#     print(sum)

# print 6 to 10
# start = 6
# stop = 10
# while start <= stop:
#     print(start)
#     start += 1

# print 1 to 5
# first loop
# start = 1
# stop = 5
# while start <= stop:
#     print(start)
#     start += 1
#     # second loop
#     start1 = 6
#     stop1 = 10
#     while start1 <= stop1:
#         print(start1)
#         start1 += 1

# hw
# create digital clock
# 1:25:0

# create multiplication table from 1 to 10
# 1 * 1 = 1
#
# 1 * 10 = 10

# importing whole module
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# root = Tk()
# root.title('clock')
# def time():
#     string = strftime('%H:%M:%s %p')
#     lbl.confing(text=string)
#     lbl.after(1000, time)
# lbl = Label(root, foot =('calibri', 40, 'bold'),
#             background = 'purple',
#             foreground = 'white')
# lbl.pack(anchor = 'center')
# time()
# mainloop()




# rows=10 # Multiplication table up to 10
# columns=10 # column values
# for i in range(1,rows+1):
#     for j in range(1,columns+1):# inner for loop
#         c=i*j
#         print("{:2d} ".format(c),end='')
#     print("\n")  # line break




