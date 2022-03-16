# a="praveen"
# c=0
# for b in (a):
#     if c%2==0:
#         print(b.upper())
#     else:
#         print(b.lower())
#     c+=1

# def greet(names):
    # for name in (names):
    #    print("Welcome", name)
# 
# a=["Rinki", "Vishal", "Kartik", "Bijender"]
# greet(a)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30}
# b=sorted(a.items(),key=lambda t:t[1],reverse=True)
# print(b)
# 
# b=sorted(a.items(),key=lambda t:t[1],reverse=True)

# Q21.Write a Python program to print all unique values in a dictionary.

# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for a1 in (a):
    # a2=(a1.values())
    # if a2 not in b:
        # b.extend(a2)
# print(b)


# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


#Q-3
# def circumference(r):
    # print(2*(22*7)*r)
# circumference(22)

#Q-4
# def power(a,b):
    # print(a**b)
# 
# power(2,4)
# Write a function to calculate power of a number raised to other. E.g.- ab.

#Q-5
# def add(a,b):
    # c=a+b 
    # return c
# 
# x=add(2,5)
# print(x)

#Q-6
# def add_numbers(number_x, number_y):
    # number_sum = number_x + number_y
    # return number_sum
# 
# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)

#Q-7
# d=["a",'g','e','f']
# b=[1,2,3,4]
# c=dict(zip(d,b))
# print(c)


#Q-8
# def f1():
#    s = "I Love Navgurukul"
#    def f2():
    #    print(s)
#    f2()
# 
# f1()


#Q-9
# def first_function():
    # s = 'I love India'
    # def second_function():
        # print(s)
    # second_function()
# first_function()

# def first_function():
    # s = 'I love India'
    # def second_function():
        # s = "MY NAME IS JACK"
        # print(s) 
    # second_function()
    # print(s)
#  
# first_function()


#Q-10
# def list1(a):
    # for a1 in (a):
        # if a1>=18:
            # print('eligible for vorte')
        # else:
            # print('not eligible')

#Q-11
# x=[]
# for a in range(5):
    # n=int(input())
    # x.append(n)
# list1(x)

# Q-12
# def perfect(b):
    # c=0
    # for a in range(1,b):



#Q-12
##print('==',a)
        # for a1 in range(1,a):
            # if a%a1==0:
                # c+=a1
                ##print(a1)
        # if c==a:
            # print(a,'is a perfect number')
        # c=0
# 
# 
# perfect(1000000000)
# 

#Q-13
# def ave(a,b,c):
    # d=a+b+c
    # return d/3
# 
# x=ave(3,4,5)
# print(int(x))


#Q-14
# def oddeve(a):
    # for a1 in range(a):
        # if a1%2==0:
            # print('even')
        # else:
            # print('odd')
# 
# oddeve(9)

#Q-15
# def sume(a):
    # c=0
    # for a1 in range(a+1):
        # if (a1%3==0) or (a1%5==0):
            # c+=a1
    # print(c)
    # c=0
# sume(15)


#Q-16
# def speed(a):
    # if a>=70:
        # c=(a-70)//5
        # if c>12:
            # print('Licence Cancel')
        # else:
            # print(c)
# 
# speed(135)


#Q-17
# def Name(a,b):
    # if len(a)>len(b):
        # print(a)
    # elif len(a)==len(b):
        # print(a)
        # print(b)
    # else:
        # print(b)
# 
# Name('praveen','welcome')
# Name('hello','praveen')

#Q-18
# def make(a1):
    # dic={}
    # for a in range(a1+1):
        # dic[a]=(a**2)
    # print(dic)
# 
# make(20)

# def primeorNot(num):
    # if num > 1:
        # for i in range(2,num):
            # if (num % i) == 0:
                # print(num,"is not a prime number")
                # print(i,"times",num//i,"is",num)
                # break
            # else:
                # print(num,"is a prime number")   
    # else:
    #    print(num,"is not a prime number")
# 
# primeorNot(406)


#Q- curd
# userDetails = {
    # '123456789': {'name':"qwert", 'email': "qwe@gmail.com", 'password':"1234567ytrdc"}
# }
# 
# def u():
    # n=int(input('enter your id'))
    # print(userDetails[n])
    # if len(userDetails) ==0:
        # print("no user data to show")
    # else:
        # userDetails.insert(n,{
        # "id":int(input("enter id")),
        # "name":input("enter name:"),
        # "email":input("enter email:")
    # })
# def delet():
    # print('enter your id ')
    # x=int(input())
    # userDetails.pop(x)
# 
# def read():
    # if len(userDetails) ==0:
        # print("no user data to show")
    # else:
        # print(userDetails)
# 
# def creat():
    # a1=int(input('enter your hone number'))
    # a = {
        # "id":int(input("enter id")),
        # "name":input("enter name:"),
        # "email":input("enter email:")
    # }
    # userDetails[a1]=a
# 
# 
# while True:
    # print("""
# press 1 for update
# press 2 for delete
# press 3 for read
# press 4 for create
# press 5 for exit
# 
# """)
    # n=int(input('Enter your option: '))
    # if n==1:
        # u()
    # elif n==2:
        # delet()
    # elif n==3:
        # read()
    # elif n==4:
        # creat()
    # elif n==5:
        # exit()
    # else:
        # print('Not Valid')
# 

# print('press 1 for login','press 2 for singin')
# n=int(input())
# # if n==1:
# #     pass

# userDetails = {}
# while True:
#     print("""
#     press 1 for update
#     press 2 for delete
#     press 3 for read
#     press 4 for create
#     press 5 for exit

#     """)
#     n=int(input('Enter your option: '))
#     if n==1:
#         n1=int(input('enter your phone no'))
#         if n1 in userDetails:
#             userDetails.update({int(input('enter ypur phone no')):{
#             'name':input("enter name"), 
#             'email':input("enter email"),
#             'password':input("enter password"),
#         }})
#     elif n==2:
#         userDetails.pop(int(input('enter your phone no')))
#     elif n==3:
#         print(userDetails[int(input('enter your phone no'))])
#     elif n==4:

#         userDetails[int(input('enter your phone no'))]=({
#             'name':input("enter name"), 
#             'email':input("enter email"),
#             'password':input("enter password"),
#         })
#     elif n==5:
#         exit()
#     else:
#         print('Not Valid')


# import json, os
# def creat():
    # 
    # if os.path.exists('pk1.json'):
        # with open("pk1.json", "r") as f:
            # data = json.load(f)
    # else:
        # data = []
    # a={
        # "name":input('Enter your Name'),
        # "roll":int(input('Enter your Roll')),
        # "email":input('Enter your Email')
    # }
    # data.append(a)
    # with open('pk1.json', "w") as f:
        # json.dump(data, f, indent=4)
# 
# creat()

# a={'name':'praveen','phone no':65532,'email':'jfue743'}
# b={'name':'praveen1','phone no':655320,'email':'jfue7430'}
# a=b
# print(a)


# b={'name':'praveen1','phone no':655320,'email':'jfue7430'}
# print(b['name'])
# print(b['phone no'])
# a=int(input())
# b=int(input())
# print(int(a/b))


a=int(input())
if a==1:
    print("chhotu")
elif a==2:
    print("praveen")
elif a==3:
    print("aniket")
elif a==4:
    print("bhumash")
else:
    print("akash")