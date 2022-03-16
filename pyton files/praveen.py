# a = 1
# b = 0
# while a <= 11 :
#     print('enter',a, "persion weight")
#     n = int(input("enter any number: "))
#     b +=n
#     a += 1
# print("average of waeght is=",b/11)
    # for b in range (1,a):
    #     print(a*c,end=" ")
    #     c=c+1or a in range (1,8)
# for a in range (1,8):
#     print(a)
#     for b in range (1,a):

#         print(a*b,end=" ")
# a=[A,B,c,D,E,F,G,H,I,J,K,L,M,N,O,O,Q,R]
# for a in range a:
#     print(a)
# banks_list = ["Kotak", "HDFc", "RBL", "SBI", "Bank of Baroda"]
# print(banks_list)
# print(type(banks_list))

# temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
# print(temperature_list)
# print(type(temperature_list))

# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print(type(mixed_list))

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]  
# print(names_list[1])

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list[0]="Praveen"
# names_list.append("dhruv")
# print("length of the list is ", len(names_list))
# print(names_list)

# n=int(input("Enter number"))
# a=1
# b=0
# while a>=n:
#     b=b+n%10
#     a=n//10
#     print(b)


# n=int(input())
# f=n
# b=0
# c=1
# while n>0:
#     e=n%10
#     for a in range (1,(e+1)):
#         c=c*a
#     print(c)
#     b=b+c
#     c=1
#     n=n//10
# print(b)
# if b==f:
#     print("Yes This is a strong number")
# else :
#     print("No it's not a strong number")


# names_list = ["abhishek", "shivam", "deepa", "rishabh", "rupa"]
# names_list. append("dhruv")
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.pop(1)
# print("length of the list is ", len(names_list))
# print(names_list)

# a=["a","b","c","d","e"]
# a.pop()
# print(a)
# print(len(a))

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("shivam" in names_list)


# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print(students_list[index])
#     index = index + 1
    
# a= ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# b=len(a)
# c=0
# while c<b:
#     print(a[c],end=(" "))
#     c=c+1

# student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
#     total_marks = student_marks[index] + total_marks
#     index = index + 1
# print("Total Marks: " + str(total_marks))

#Miraki qustion Date(17,1,2022)
#Q-1
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(len(numbers))

#Q-2
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=0
# while a<len(numbers):
#     b=(numbers[a])
#     if b>20 and b<40:
#         print(b)
#     a+=1


#Q-3
# a=0
# c=0
# e=0
# while a<len(numbers):
#     b=numbers[a]
#     if c<b:
#         c=b
#         # print(c,end=(", "))
#     if c<b:
#         print(c)
#     a+=1

#Q-4
# n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=0
# b=0
# while a<len(n):
#     # print(n[a])
#     print(len(a))
#     a=a+1


# Q-5
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))

#Q-6(sec max number)
# numbers = [50, 40, 23, 70, 56, 12, 5, 72, 10, 7]
# n=max(numbers)
# numbers.remove(n)
# print(max(numbers))


# Q-7(Print Places Of Lst)
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# for a in range(len(places)):
     # print(places[a])
    
    
# Q-8
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# places.reverse()
# print(places)

#Q-9
# a = [1,2,3,4,5,6]
# b = [2,3,1,0,6,7]
# for c in range (len(a)):
    # d=(a[c])
    # if d not in b:
        # print(d)
        
# Q-10        
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# f=[]
# b=0
# for a in range(len(n)):
#     c=(n[a])
#     for b in range (len(n)):
#         e=(n[b])
#         if (c+e)==30:
#             print(n[a],n[b])
        
            
#Q-11
# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faical', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# for a in range(len(students)):
    # print(students[a],marks[a])
    
# Q-11
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=[]
# c=[]
# for a in range(len(n)):
    # e=n[a]
    # if e%2==0:
        # e=1
        # b.append(e)
    # else:
        # e=0
        # c.append(e)
# print("number of even number",b.count(1))
# print("number of odd number",c.count(0))

#Q-12
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# c=0
# for a in range(len(n)):
    # e=n[a]
    # if e%2==0:
        # b=b+e
    # else:
        # c=c+e
# print("sum of even number",b)
# print("sum of odd number",c)

#Q-13
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# f=0
# c=0
# g=0
# for a in range(len(n)):
    # e=n[a]
    # if e%2==0:
        # b=b+e
        # e=1
        # g=g+e
    # else:
        # c=c+e
        # e=1
        # f=f+e
# print("sum of even number",b,b/g)
# print("sum of odd number",c,c/f)


#Q-14
# a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# b=[]
# for c in range(len(a)):
    # d=a[c]
    # if d not in b:
        # b.append(d)
# print(b,)

#Q-15
# count of odd numbers ….
# count of even numbers ….
# count of all the numbers ….
# sum of odd numbers ….
# sum of even numbers ….
# sum of all the numbers ….
# average of odd numbers ….
# average of even numbers ….
# average of all the numbers ka …
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# c=[]
# e=0
# f=0
# g=0
# d=[]
# for a in range(len(n)):
    # b=(n[a])
    # g+=b
    # if b%2==0:
        # e+=b
        # c.append(b)
    # else:
        # f+=b
        # d.append(b)
# print("number of odd numbers",len(d))
# print("numbers of even numbere",len(c))
# print("sum of even number",e)
# print("sum of odd number",f)
# print("all element of n",len(n))
# print("Sum of all numbers",g)
# print("average of even number",e/len(c))
# print("average of odd number",f/len(d))
# print("average of all number",g/len(n))

#Q-16
# a = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# d=[]
# e=[]
# f=[]
# for b in range(len(a)):
    # c=(a[b])
    # if c>=100000 and c<=10000000:
        # d.append(c)
    # elif c>=10000000 and c<=1000000000:
        # e.append(c)
    # else:
        # f.append(c)
# print("Dilwale",len(f))
# print("crorepati",len(e))
# print("Lakhpati",len(d))


#Q-17
# a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# d=[]
# for b in range (len(a)):
    # c=a[b]
    # if c not in d:
        # d.append(c)
# for e in range(len(d)):
    # f=d[e]
    # print(d[e],a.count(f),"Times")
    
#Q-18
# n= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# n.sort()
# b=[]
# for a in range(len(n)):
    # c=n[a]
    # if c not in b:
        # b.append(c)
# print(b)

#codesdope Qustion
#Q-19
# a=[]
# for b in range(10):
    # a.append(int(input()))
# print(a)

#Q-20
# a=[]
# for b in range(10):
    # a.append(int(input()))
# print("Orignal list is ",a)
# n=int(input())
# if n in a:
    # print("Yes this number in a")
# else:
    # print("No is number is not in a")


#Q-21
# a=[]
# for b in range (20):
    # a.append(int(input()))
# print(a)
# f=[]
# e=[]
# d=[]
# g=0
# h=0
# for b in range(len(a)):
    # c=a[b]
    # print(c)
    # if c==0:
        # d.append(c)
    # elif c>0:
        # e.append(c)
    # else:
        # f.append(c)
    # if c%2==0:
        # g=g+(c/c)
    # if c%2!=0:
        # h=h+(c/c)
# print("number of positive number",len(e))
# print("number of nagitive number",len(f))
# print("number of cero number",len(d))
# print("Number of odd numbers",h)
# print("number of even number",g)


#Q-22
# a=[]
# for b in range(10):
    # a.append(int(input()))
# print("Orignla data",a)
# a.reverse()
# print("reverse element list",a)

#Q-23
# a=[]
# c=0
# for b in range(10):
    # a.append(int(input()))
    # c+=a[b]
# print("Orignla data",a)
# a.reverse()
# print("reverse element list",a)
# print("Sum of all element",c)

#Q-24
# a=[[1,2,3],[4,5,6]]
# i = 0
# while i<len(a):
#   j = 0
#   while j < len(a[i]):
    # print(a[i][j])
    # j = j+1
#   i = i+1

#Q-25
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# n.sort()
# print(n[0],n[-1])

#Q-26
# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# for a in (n):
    # b+=a
# n.sort()
# print("sum of number",b)
# print("average of number",b/len(n))
# print("small number of list",n[0])
# print("largest number of list",n[-1])


#Q-27
# n=[2,3,15,15,3,2,4]
# for a in (n):
    # n.remove(a)
    # if a in n:
        # print("Yes this element more then one",a)
    # else:
        # print("No this element only one",a)
        
#Q-28
# n=[1,2,3,2,1,3,12,12,32]
# b=[]
# for a in (n):
    # if a not in b:
        # b.append(a)
# print("not repited element",b)

#Q-29
# a=[58,24,13,15,63,9,8,81,1,78]
# d=len(a)//2
# c=[]
# e=[]
# for b in range (d):
    # c.append(a[b])
# print(c)
# a.reverse()
# for b in range (d):
    # e.append(a[b])
# print(e)

#Q-30
# a=[]
# for b in range (10):
    # c=int(input())
    # if c%2==0:
        # a.append(c)
# print(a)

#Q-31
# a=[1,2,3,4,5]
# a.reverse()
# print(a)

# fruits = ['apple', 'banana', 'cherry']
# points = [1, 4, 5, 9]
# # fruits.extend(points)
# fruits.insert(1,"Mango")
# print(fruits)     
# ]]
# a = [[11,12,13],[14,13],[13,29,59,[11,12,[55,56,57]]]]
# c=[]
# d=[]
# for b in (a):
#    c.extend(b)
# print(c)
# for e in (c):
    # d.extend(e)
# print(d)

# a=[11,9,13,14,45,12,8,13,7]
# g=0
# for b in range (len(a)):
    # e=a[b]
    # for c in range (len(a)):
        # f=a[c]
        # if e+f==20:
            # print(a[b],a[c])
            # g=g+1
# print("combination ",g)

# a=[11,12,33,44,55,67,67]
# b=max(a)
# for c in range(a.count(b)):
    # for d in range(c):
        # a.remove(b)
# print(a)

# b=[]
# for c in (a):
    # if c not in b:
        # b.append(c)
# b.sort()
# print("first max number",b[-1],"sec max no",b[-2],"third max no",b[-3])

# b=[99,98,11,44,77,78,88,99]

# e=[]
# f=0
# for c in range(100,0,-1):
#     if c in b:
#         f=b.count(c)
#         for g in range(f):
#             e.append(c)
# print(e)


# for i in range(len(b)):
    # for j in range(i+1,len(b)-1):
        # print(b[i],b[j])
        # if b[j]>b[i]:
            # b[i],b[j]=b[j],b[i]
            # print(b[i],b[j])
# print(b)

# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits=[]
# print(fruits)

#Q-32
# 
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
##list1.extend(list2) 
# list3=list1+list2
# print(list3)

#Q-33
# n=[100,200,300,400,500,700,600,700,600,500,700]
# b=0
# c=0
# for a in (n):
    # if a==700:
        # b+=a
    # elif a==600:
        # c+=a
# print("sum of 700=",b)
# print("sum of 600=",c)


# a=[11,21,[302,[12,3,4],403,502,35,42]]
# c=[]
# for b in (a):
    # 
    # c.extend(b)
    # c.extend([b])
    # if type(b)== list:
        # for i in b:
            # print(i)
            # c.append(i)
    # else:
        # print(b)
        # c.append(b)
    # 
# print(c)
# print(type(a))

# a=1
# while a<=5:
    # a+=1
# print(a-1)

# a=1
# b=10
# c=2
# for n in range (a,b,c):
#     print(n)
    
# a=1
# while a<=20:
    # if a%2!=0:
        # continue
    # print(a)
    # a=a+1
    
# a=1
# while a<=20:
    # if a%2!=0:
        # continue
    # print(a)
    # a+=1

# from ast import If


# a=1 
# while a<=20:
    # if a%2==1:
        # continue
    # print(a)
    # a=a+1
    
# a=1
# while a<=20:
    # a=a+1
    # if a%2!=0:
        # continue
    # print(a)
    # 
    

# n=int(input())
# a=0
# while a<=n:
    # a+=1
    # if (a%2==0 and a!=2) or (a%3==0 and a!=3) or (a%5==0 and a!=5) or (a%7==0 and a!=7) or (a%11==0 and a!=11) or (a%13==0 and a!=13) or (a%17==0 and a!=17):
        # continue
    # print(a)
    # 
# for a in range(0,101,2):
    # print(a)
# for b in range(1,102,2):
    # print(b)
    # 
# a=1
# b=str()
# c=str()
# while a<=200:
    # if a%2==0 and a<100:
        # print(a)
    # elif a%2!=0 and a>100:
        # print(a-100)
    # a+=1
# print(b)
# print(c)


# n=int(input())
# a=len(str(n))
# d=[]
# c=1
# while c<=n:
    # d.append(n%10)
    # c=n//10
# print(d)

# n=int(input())
# f=n
# sum=0
# while n>0:
    # sum=(sum*10)+(n%10)
    # n=n//10
# if f==sum:
    # print("palidrom Number")
# else:
    # print("is not a palidrom number")

# n=int(input())
# b=n
# a=0
# while n>0:
    # a=(a*10)+(n%10)
    # n=n//10
# if a==b:
    # print("yes this is pladrom number")
# else:
    # print("This is not palidron number")

# a=5
# while a>0:
#     b=a
#     while b>0:
#         if b>1:
#             print(b,end=" ")
#         else:
#             print(b)
#         b-=1
#     a-=1
    
    
    #Dictionary (date(23-1-22))
#creat a dictionary
# d={"brand":"sucuki","modul":"Dicair","year":2020,}
# for a,c in (d.items()):
    # print(a)
    # print(c)
# print("Dicair" in d["modul"])
# print(len(d))

#len(in dictionary)
# d={"brand":"sucuki","modul":"Dicair","year":2020,}
# print(len(d))

#pop(in dictionay)
# d={"brand":"sucuki","modul":"Dicair","year":2020,}
# d.pop("modul")
# print(d)

#del (in dectionary)
# d={"brand":"sucuki","modul":"Dicair","year":2020,}
# del d["year"]
# print(d)

#copy (in dectionary)
# d={"brand":"sucuki","modul":"Dicair","year":2020,}
# x=d.copy()
#    or 
# x=d
# print(x)

#creat a dictionary using two variable
# a=("Praveen","Kumar","bast","Motiation")
# b=1
# d={}
# d=d.fromkeys(a,b)
# print(d)


#stdefoult(in dectionary)
# a={"Praveen":"Kumar","bast":"Motiation"}
# b=(a.setdefault("Prakash","k"))
# print(a)
# print(index(b))

#
# n=int(input())
# a=0
# b=0
# while n>0:
#     b=n%2
    # a=
# 
# dic= {'Name': 'RAM','Age': 17,}
# dic['ORGANIcATION']="NAV GURUKUL"
# dic['place']='dharamsala'
# print(dic)
# print(dic.items())
# for x in (dic.values()):
    # print(x)
    # for y in (dic):
        # print(y)
# for x,y in (dic.items()):
    # print(x,y)
# dic.popitem()
# print(dic)
# x=dic.setdefault('place','dharamsala')
# print(dic)
# dic.update({'colore':'red'})
# print(dic)
# print(len(dic))
# print(dic.items())
# 
# 
# fruit = {"mango": 40, "banana": 10}
# print(fruit.get("cherry", 50))
# print(fruit)
# 
# mydict = {'name': 'John', 'age': 45}
# mydict.update(gender = 'male')  # adding a new key-value pair
# print(mydict)  # printing changed dictionary
# 
# 
# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# for k, v in mydict.items():
    # print("key =", k)
    # print("value =", v)
    # 
    # 
# dict1 = {'a': 20, 'b': 10, 'c': [1, 2, 3]}
# d=dict1
# dict2 = dict1
# dict2['b'] = 30
# dict2['c'] = [1, 2, 3, 4]
# print("Original dictionary:", dict1)
# print("New dictionary:", dict2)
# print(d)
# 
# 
# dict1 = {'a': 20, 'b': 10, 'c': [1, 2, 3]}
# dict2 = dict1.copy()
# dict2['b'] = 30
# dict2['c'] = [1, 2, 3, 4]
# print("Original dictionary:", dict1)
# print("New dictionary:", dict2)
# 
# 
# dict1 = {'a': 20, 'b': 10, 'c': [1, 2, 3]}
# dict2 = dict(dict1)
# dict2['b'] = 30
# dict2['c'] = [1, 2, 3, 4]
# print("Original dictionary:", dict1)
# print("New dictionary:", dict2)
# 
# mydict = {'a': 20, 'c': [1, 2, 3],'b': 10}
# print(sorted(mydict))
# x=sorted(mydict)
# print(x)
# 
# mydict = {2: 'John', 1: 45, 3: 'male'}
# print(sorted(mydict, reverse=True))
# print(any(mydict))
# 
# cubes = {num: num**3 for num in range(1, 11)}
# print(cubes)
# 


#today dictionary questioln(24-1-22)
#Q-1
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic= {}
# for i in [dic1,dic2,dic3]:
    # print(i)
    # for j in i:
        # print(j)
        # dic[j]=i[j]
# print(dic)
# print(list(dic2.items()))

        #  or 
        
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# d={}
# for a in (dic1,dic2,dic3):
    # d.update(a)
# print(d)    
    
    
#Q-2
# dict1={'name':'Raju', 'marks':56}
# for n in (dict1.keys()):
    # if n=='name':
        # print("exist")
    # else:
        # print("not exist")
        
#Q=3
# dict = {'data1':100,'data2': -54,'data3': 247}
# b=0
# for n in (dict.values()):
    # b+=n
# print(b)

#Q-4
# Dic= {1:'NAVGURUKUL',2:'IN',3:{'A':'WELcOME','B':'To','c':'DHARAMSALA'}}
# Dic[3].pop('A')
# print(Dic)

#Q-5
# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# d={}
# for i in range(len(list1)):
    # d[list1[i]]=list2[i]
    # print(d)
    # or
# for a in range(5):
    # d.setdefault(list1[a],list2[a])
# print(d)

#Q-6
# dic={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3}
# dic['ball']='red'
# dic['bat']=4
# print(dic)

#Q  -7
# n=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# g={}
# for f in (n):
    # g.update(f)
# a=[]
# for h in (g.values()):
    # a.append(h)
# e=[]
# for b in (a):
    # c=(a.count(b))
    # if c<2:
        # e.append(b)  
# for b in (a):
    # c=(a.count(b))
    # if c==2 and b not in e:
        # e.append(b)
# print(e)     
# a={}
# for b in range(1,11):
    # print("Enter",b,"Student Name")
    # x=input()
    # print("Enter",b,"Student Nimber")
    # y=input()
    # a.setdefault(x,y)
# print(a)

#Q-8
# a="MISSISSIPPI"
# e={b:a.count(b) for b in (a)}
# print(e)

#Q-9
# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
# b=[]
# for a in (dict1.values()):
    # b.extend(a)
# print(len(b))

#Q-10
# a = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# c=[]
# for b in (a.values()):
    # c.append(b)
# c.sort()
# print(c[3:])

#Q-11
# a={a:a**2 for a in range(1,16)}
# print(a)

#Q-12
# a = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
# b=sorted(a.items(),key=lambda t:t[1])
# print(b)
# b.reverse()
# c={}
# c=(dict(b))
# print(c)
# f=[]
# for e in (c.keys()):
    # f.append(e)
# print(f[:3])
       #or
#(Dictionary short)
# markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist=list(markdict.items())
# print(marklist)
# l=len(marklist)
# for i in range(l-1):
    # for j in range(i+1,l):
        # if marklist[i][1]>marklist[j][1]:
            # t=marklist[i]
            # marklist[i]=marklist[j]
            # marklist[j]=t
    # sortdict=dict(marklist)
# print(sortdict)

#Q-13
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# b=sorted(a.items(),key=lambda t:t [1])
# b.reverse()
# c=(dict(b))
# print(c)

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)

#Q
# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# d={}
# for a in range(5):
#    d[list1[a]]=(list2[a])
# print(d)

#Q
# a = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
# b=sorted(a.items(),key=lambda t:t [1])
# c=(b[3:])
# c.reverse()
# e=(dict(c))
# print(e.keys())

#Q-14
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# c=[]
# for b in range(100):
    # if b in (a.values()):
        # c.append(b)
# print(c)
# 
# b=(list(a.items()))
# print(b)
# e=[]
# for c in (b):
    # e.extend(c)
# e.sort()
# print(e)
# print(a.items())
# for i in a.items():
#     print(i[1])
#     for b in range(100):
#         if b in (i[1]):
#             print(b)

# fruit={}
# def addone(index):
    # if index in fruit:
        # fruit[index] += 1
    # else:
        # fruit[index] = 1
        # 
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# 
# print(len(fruit))
# print(fruit)
# 
# a={}
# def b(index):
    # if index in a:
        # a[index]+=1
    # else:
        # a[index]=1
# b('praveen')
# b('amit')
# b('aman')
# b('amit')
# b('karan')
# 
# print(a)

#Sort Without using sort in dictionary

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# main_list =[]
# for i in list(a.items()):
    # lis=[]
    # for j in i:
        # lis.append(j)
    # main_list.append(lis)
##    print(lis)
##print(main_list)
# for i in range(len(main_list)):
    # for j in range(i+1,len(main_list)):
        # a = main_list[i][1]
        # b=main_list[j][1]
        # if a>b:
            # main_list[i][1],main_list[j][1]=main_list[j][1],main_list[i][1]
  ##      print(a,b)
# print(dict(main_list))


#Date(27-1-22) codedope Question    
#Level 1
#Q-1
# c={}
# for a in range(1,101):
    # print('Enter',a,'Student name other wise press e')
    # n=input()
    # print('Enter',a,'Student Marks')
    # b=input()
    # if n!='e':
        # c.setdefault(n,b)
    # else:
        # break
# print(c)


#Q-2
# c={}
# for a in range(1,101):
    # print('Enter',a,'Student name other wise press e')
    # n=input()
    # print('Enter',a,'Student Marks')
    # b=int(input())
    # if n!='e':
        # c.setdefault(n,b)
    # else:
        # break
# print(c)
# b=sorted(c.items(),key=lambda t:t [1])
# print(b)

#Q-3
# a='MISSISSIPPI'
# b={b:a.count(b) for b in (a)}
# print(dict(sorted(b.items(),key=lambda t:t [1])))

#Q-4
# d={'Absence':'Presence','Accept':'Refuse','Accurate':'Inaccurate','Advantage':'Disadvantage','Alive':'Dead','Ancient':'Modern','Answer':'Question'}
# n={}
# for a,b in (d.items()):
    # n.setdefault(b,a)
# print(n)

#Q-5
# d={'Absence':'Presence','Accept':'Refuse','Accurate':'Inaccurate','Advantage':'Disadvantage','Alive':'Dead','Ancient':'Modern','Answer':'Question'}
# print(d.keys())
# n=input('')
# print(d[n])

#Q-6
# a=["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# n={'a':[3],'b':[88],'c':[88],'d':[7,8,3]}
# b={}
# v=[]
# for x in (n.values()):
    # v.extend(x)
    # for c in (v):
        # lis = []
        # for i in (n.keys()):
            # if c in (n[i]): 
                # lis.append(i)
                # b[c]=lis
# print(b)

#date(w3resours)
#Q_2
# n={0: 10, 1: 20}
# n.update({2:30})
# print(n)

#Q-3
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for a in (dic1,dic2,dic3):
    # dic4.update(a)
# print(dic4)


#Q-4
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for a in (dic1,dic2,dic3):
    # dic4.update(a)
# print(dic4)
# n=int(input())
# if n in (dic4):
    # print("yes")
# else:
    # print("No")
    
    
#Q-6
# n=int(input())
# B={a:a**2 for a in range(1,(n+1))}
# print(B)

# Q-7
# n=15
# B={a:a**2 for a in range(1,(n+1))}
# print(B)

# Q-8
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic1.update(dic2)
# print(dic1)

#Q-9
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for a,b in (d.items()):
    # print(a,"corresponds to",b)

#Q-10
# n= {'data1':100,'data2':-54,'data3':247}
# c=0
# for a in (n.values()):
    # c+=a
# print(c)

#Q-11
# n= {'data1':100,'data2':-54,'data3':247}
# b=2
# for a in range(b):
    # print(n)
    
#Q-12
# n= {'data1':100,'data2':-54,'data3':247}
# b=input()
# n.pop(b)
# print(n)

#Q-13
# m=[1,4,9,16,25,36,49]
# n=[1,2,3,4,5,6,7]
# p={}
# for a in range(len(m)):
    # p[n[a]]=m[a]
# print(p)

#Q-14
# n={1: 49, 2: 36, 3: 25, 4: 16, 5: 9, 6: 4, 7: 1}
# x=sorted(n.items(),key=lambda t:t [1])
# print(x)

#Q-15
# n={1: 49, 2: 36, 3: 25, 4: 16, 5: 9, 6: 4, 7: 1}
# print(max(n.values()))
# print(min(n.keys()))

#Q-16
# s={'id1':{'name':['Sara'],'class':['V'],'subject_integration':['english,math,science']},'id2':{'name':['David'],'class':['V'],'subject_integration':['english,math,science']},'id3':{'name':['Sara'],'class':['V'],'subject_integration':['english,math,science']},'id4':{'name':['Surya'],'class':['V'],'subject_integration':['english,math,science']},}
# b={}
# for a,b in (s.items()):
    # b.setdefault(a,b)
# print(b)

# Q-17
# n={1:21,2:45,3:21,4:47,5:45,6:84}
# v=[]
# c={}
# for a,b in (n.items()):
    # if b not in v:
        # v.append(b)
        # c[a]=b
# print(c)

#Q-18
# b={}
# if len(b)==0:
    # print('Empty')
# else:
    # print('not empty')

#Q-19
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d=counter(d1)+counter(d2)
# print(d)


#Q-20
# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# e=[]
# f=[]
# for b in (a):
    # c=(b.values())
    # e.extend(c)
# print(e)
# for g in (e):
    # if g not in f:
        # f.append(g)
# print(f)

#Q-21
# a={'1':['a','b'], '2':['c','d']}
# for b in (a['1']):
    # for c in (a['2']):
        # print(b,c)
        
#Q-22
# m = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# b=[]
# for c in (m.values()):
    # if c not in b:
        # b.append(c)
# b.sort()
# print(b[2:])

#Q-23
# a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# c={}
# for b in a:
    # if b['item'] not in c:
        # c[b['item']]=b['amount']
    # else:
        # c[b['item']] = c[b['item']] + b['amount']
# print(c)

#Q-24
# a='w3resource'
# c={b:a.count(b) for b in (a)}
# print(c)

#Q-25
# a = {'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
# for b in (a.keys(),a['c1'],a['c2'],a['c3']):
    # print(b)

#Q-26
# s = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# d=0
# for a in (s):
    # c+=a['id']
    # d+=a['success']
# print(c,d)

#Q-27
# n = [1, 2, 3, 4]
# b=current ()
# for a in (n):
    # current[b]={}
    # current=current[b]
# print(b)

#Q-28
# n = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# m={}
# for a,b in (n.items()):
    # m[a]=sorted(b)
# print(m)
# 

#Q-29


#Q-30
# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# b=sorted(a.items(),key=lambda t:t [1],reverse=True)
# print(b[:3])

#Q-31
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print('key','values','count')
# for a,b in (d.items()):
    # print(a, b, a)

#Q-32
# s = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for a,b in (s.items()):
    # print(a)
    # for c in (b.items()):
        # print(c)

#Q-34
# d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# e=[]
# for a in (d.values()):
    # e.extend(a)
# print(len(e)) 

#Q-35
# d={'Math':81, 'Physics':83, 'chemistry':87}
# x=(list(d.items()))
# x.reverse()
# d=(dict(x))
# print(d)    

#Q-36
# d= ['class-V', 'class-VI', 'class-VII', 'class-VIII'], [1, 2, 2, 3]
# b=[]
# c=[]
# for a in range(2):
    # if a ==1:
        # b.extend(d[a])
    # else:
        # c.extend(d[a])
# print(b)
# print(c)
# e={}
# for i in range(4):
    # e[c[i]]=b[i]
# print(e)

#Q-37
# a={'key1': 1, 'key2': 3, 'key3': 2}
# b={'key1': 1, 'key2': 2}
# c={}
# for d,e in (a.items()):
    # for f,g in (b.items()):
        # if d==f and e==g:
            # print(f,g)
            # 
            
#Q-(Pawan)
# g=['employee 1','employee 2','employee 3']
# b=['Name','Age','Designation']
# c=[['Aman','32','HR'],['Abhisak','28','Exicutive'],['Karan','24','Accountant']]
# f=[]
# for a in range(len(c)):
#     e={
#         b[0]:c[a][0],
#         b[1]:c[a][1],
#         b[2]:c[a][2]
#     }
#     f.append(e)
#     x=cip(g,f)
#     print(dict(x))
# print(f)
# n={}
# for i in range(len(g)):
#     n[g[i]]=f[i]
# # print(n)
# 
# for i in range(len(c)):
    # n["employee "+str(i+1)] = f[i]
# print(n)

# n=[a for a in range(5)]
# print(n)
# for i in cip(g, f):
#     print(i)

#Q-(Geeks for geeks)
# test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
            #  'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}
# res=dict()
# for key, val in test_dict.items():
    # for key_in, val_in in val.items():
        # if key_in not in res:
            # temp = dict()
        # else:
            # temp = res[key_in]
            # temp[key] = val_in
            # res[key_in] = temp
# print(str(res))
# 
# res = dict()
# for key, val in test_dict.items():
    # for key_in, val_in in val.items():
        # if key_in not in res:
            # temp = dict()
        # else:
            # temp = res[key_in]
        # temp[key] = val_in
        # res[key_in] = temp
# print(str(res))

# n=int(input())
# b=[a for a in range(1,n+1)]
# g=[b for b in range(1,n+1,n)]
# h=[]
# print(b)
# print(g)
# m=int(input())
# for c in (b):
    # if c not in g:
        # print(c)
        # h.append(c)
# print(h)


# n=34564567
# a=n%1000
# d=n-a
# e=n//1000
# f=n%100
# b=a//100
# g=f*10+b
# c=e*1000+g
# print(n)
# print(a)
# print(d)
# print(e)
# print(f)
# print(b)
# print(g)
# print(c)


# n=int(input())
# a=[a for a in range(1,n+1)]
# print(a)
# b=int(input())

# print('How much no is list')
# n=int(input())
# a=list(range(1,n+1))
# print('Which no multipal do you want remove')
# m=int(input())
# g=[]
# for b in a:
    # if b%m!=0:
        # g.append(b)
# print(g)
# a=list(range(1,20,3))
# for b in range(1,10,2):
    # a.append(b)
# print(a)
# a=1
# while a<10:
    # a=a+3
    # print(a)
    
# a=0
# b=1
# c=1
# n=int(input())
# m=int(input())
# counter = 0
# for d in range(2,100):
    # if c%n==0:
        # counter +=1
        # if counter == m:
            # print('index',d,'val',c)
    # a=b
    # b=c
    # c=a+b


# a=[10,11,12,13,14,17,18,19]
# e=[]
# for b in (a):
    # for c in (a):
        # if b+c==30:
            # e.append([b,c])
            # a.remove(b)
# print(e)

# a=list(range(12))
# c=1
# for b in a:
    # if b%5!=0:
        # print(b,end=" ")
    # else:
        # print(b)  
# 
# a=['what is my name','who is prasident of india','what is capital of india']
# b=[['1=praveen','2=anikat','3=akash','4=ranveer'],['1=Modi','2=ramnath govind','3=akhilash','4=lalu'],['1=Bihar','2=Rajesthan','3=Delhi','4=Gujrat']]
# e=[]
# for c in range(3):
    # print(a[c])
    # for i in
    # print(b[c])
    # e.append(int(input()))
# print(e)
# g=[1,2,3]
# h=0
# for f in e:                 
    # if f in g:
        # h+=100
# print('Win Amount',h)
# 


# 
# a=['1.what is my name?',
    # '2.who is prasident of india?',
    # '3.what is capital of india?',
    # " 4.How many continents in the world?",
    # " 5.Which day is observed as the world standard day?",
    # " 6.what is the national food of Navgurukul?",
    # " 7.Who is the author of the epic 'Magdoot'?",
    # " 8.September 27 is celebrated every year as?",
    # " 9.How many planets are there in our solar system?",
    # " 10.Who is the president of America?",]
# 
# 
# b=[ ['1=praveen','2=anikat','3=akash','4=ranveer','5=Life line'],
    # ['1=Modi','2=ramnath govind','3=akhilash','4=lalu','5=Life line'],
    # ['1=Bihar','2=Rajesthan','3=Delhi','4=Gujrat','5=Life line'],
    # ["1=1","2=5","3=4","4=7","5=Life line"],
    # ["1=June 26","2=Oct 14","3=Nov 15","4=Dec 2","5=Life line"],
    # ["1=Rice","2=Fried","3=Fried Rice","4=Dal","5=Life line"],
    # ["1=Vamlmiki","2=Banabhata","3=Kalidas","4=Vishal","5=Life line"],
    # ["1=Teacher,s Day","2=Natinal Integretion Day","3=World Tourism Day","4=International Day","5=Life line"],
    # ["1=5","2=8","3=9","4=6","5=Life line"],
    # ["1=Joe Biden","2=Donald Trump","3=Emmanuel Macron","4=Barack Obama","5=Life line"],]
# e=[]
# j=[[2,4],[1,3],[1,4],[2,4],[2,3],[2,3],[3,1],[4,1],[2,4],[4,1]]
# life=['1).50:50','2).Phone-a-Friend','3).Audience Poll','4).Switch the Question']
# life1=0
# life2=0
# life3=0
# life4=0
# y=0
# g=[1,2,3,4,2,3,3,3,2,1]
# for c in range(len(a)):
    # print(a[c])
    # for i in range(5):
        # print(b[c][i])
    # if life1==1:
        # print('already uesed 50:50')
    # if life2==1:
        # print('already uesed Phone a friend')
    # if life3==1:
        # print('already uesed Audience Poll')
    # if life4==1:
        # print('already uesed Switch the Question')
    # k=int(input())
    # if k==5:
        # for li in (life):
            # print(li)
        # lif=int(input())
        # if lif==1 and life1<1:
            # print('incorrect Answear',j[c])
            # l=int(input())
            # e.append(l)
            # life.remove('1).50:50')
            # life1+=1
        # elif lif==2 and life2<2:
            # print('correct Answear',g[c])
            # l=int(input())
            # e.append(l)
            # life.remove('2).Phone-a-Friend')
            # life2+=1
        # elif lif==3 and life3<1:
            # print('correct Answear',g[c])
            # l=int(input())
            # e.append(l)
            # life.remove('3).Audience Poll')
            # life3+=1
        # elif lif==4 and life4<1:
            # print('correct Answear',g[c])
            # l=int(input())
            # e.append(l)
            # life.remove('4).Switch the Question')
            # life4+=1
        # y+=1
        # if l==g[c]:
            # print('you won 100 rs')
        # else:
            # print('you lose')
    # elif k==5 and y==1:
        # print('already used our Life line')
        # l=int(input())
        # e.append(l)
        # if l==g[c]:
            # print('you won 100 rs')
        # else:
            # print('you lose')
    # else:
        # l=k
        # e.append(k)
        # if l==g[c]:
            # print('you won 100 rs')
        # else:
            # print('you lose')
# print('Your Answear')
# print(e)
# 
# h=0
# for a in range(len(g)):
    # if e[a]==g[a]:
        # h+=100
# print('Win Amount',h)

# 
# def sum():
    # c=0
    # for i in (a[b]):
        # c+=i
    # print(c)
        #  
# a=[[8,7,6]
#    ,[5,4,3,]
#    ,[2,1,0]
#    ]
# print(sum(0))
# print(sum)

# a=['what is the capital of india','what is my name']
# b=[['1).Delhi','2).Bihar','3)Himachal','4).Gujrat'],['1).Mr. Raja','2).Praven','3).Aniket','4).Bhumesh']]
# for a1 in range(len(a)):
    # print(a[a1])
    # for a2 in (b[a1]):
        # print(a2)
    # n=int(input())

#date(6-2-22)meraki qustion funtion

# def add_numbers(number1, number2):
    # print("I will add two numbers.")
    ##print(number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)

# def say_hello_people(name_x, name_y, name_z, name_a):
    # print("Namaste ", name_x) # In hindi
    # print("Alah hafiz ", name_y) # In urdu 
    # print("Bonjour ", name_z) # In french 
    # print("Hello ", name_a) # In english 
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")


#Q-2
# def a():
    # print('My nname is Praveen')
    # print('I am student of navgurukul')
    # 
# a()

#Q-3
# def a(a1,a2=20):
    # print(a1+a2)
# a(12) 


#Q-4
# def add(a1,a2):
    # print(a1+a2)
    # 
# num1 = 56
# num2 = 12
# add(num1,num2)


#Q-5
# def add(a,b):
    # for c in range(len(a)):
        # print(a[c]+b[c])
# 
# list1=[50, 60, 10]
# list2=[10, 20, 13]
# add(list1,list2)

#Q-6
# def chack(a,b):
    # if a%2==0 and b%2==0:
        # print('Both are even')
    # else:
        # print("both numbers are not even")
# chack(2,8)

#Q-7
# def chack(a,b):
    # for c in range(len(a)):
        # if a[c]%2==0 and b[c]%2==0:
            # print('Both are even')
        # else:
            # print("both numbers are not even")
        # 
# a=[2, 6, 18, 10, 3, 75]
# b=[6, 19, 24, 12, 3, 87]
# chack(a,b)
# 
#Q-8
# def call(a,b,c):
    # if c=="add":
        # print(a+b)
    # elif c=="Subtract":
        # print(a-b)
    # elif c=="Multiply":
        # print(a*b)
    # elif c=="Divide":
        # print(a/b)
# 
# call(2,6,"add")


#Q-9
# def call(a,b,c):
    # if c=="add":
        # print(a+b)
    # elif c=="Subtract":
        # print(a-b)
    # elif c=="Multiply":
        # print(a*b)
    # elif c=="Divide":
        # print(a/b)
# 
# call(2,6,"add")


#Q-10
# def call(a):
    # c=[]
    # d=[]
    # e=[]
    # c.extend(a[0])
    # d.extend(a[1])
    # for a1 in range(4):
        # e.append(c[a1]*d[a1])
    # print(e)
    # 
# 
# a=[[5, 10, 50, 20],[2, 20, 3, 5]]
# call(a)

# d={}
# for a in range(10):
    # n=input()
    # n1=input()
    # d[n]=n1
# print(d)


#(prograss traking)
#Q-1
# print(chr(65))
# a=input()
# caps = [chr(i) for i in range(65, 91)]
# nim=[str(i1) for i1 in range(10)]
# caps1=[chr(i) for i in range(97,122)]
# o1=0
# o2=0
# o3=0
# for ai in (a):
    # if ai in (nim):
        # o1+=1
    # elif ai in (caps):
        # o2+=1
    # elif ai in (caps1):
        # o3+=1
# print('capital alphabet',o2)
# print('Nombers',o1)
# print('small alphabet',o3)



# for a in range(1,10):
    # print((10*a//9)*2)
    # 
# for a in range(1,9):
    # for a1 in range(1,a):
        # print(a1,end=" ")
    # print()
    
# def table(n,i):
    # print (n*i)
    # i=i+1
    # if i<=10:
    #   table(n,i)
    #   
    #   
# table(12,5)

# def rectangle(a):
    # print(' area and perimeter of a rectangle.',a*4)
# 
# rectangle(4)


# ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')


# from decimal import Decimal
# from re import I


# def well(x):
    # if x.count('good')==0:
        # y='Fail!'
    # elif x.count('good')<3:
        # y='Publish!'
    # else:
        # y='I smell a series!'
    # return y

# x=['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']
# z=well(x)
# print(z)


# def alphabet_position(text):
    # q=text.upper()
    # caps = [chr(i) for i in range(65, 91)]
    # c=''
    # for a in (q):
        # if a in caps:
            # w=ord(a)
            # print(str(w-64),end=" ")
        # else:
            # pass
# 
# alphabet_position("The sunset sets at twelve o' clock.")

# a=[1,2,3,[4,5,6,7,[8,9,10,[11,12,13]]]]
# # a1=[]
# # for a2 in (a):
# #     if type(a2)==list:
# #         for j in (a2):
# #             if type(j)!=list:
# #                 for j1 in (j):
# #                     a1.append(j1)
# #     else:
# #         a1.append(a2)
# # print(a1)

# a=[1,[2,[3,4]]]
# b=[]
# for i in a:
    # b=a.extend(i)
    # print(b)
    # if type(i)==list:
        # b.extend(i)
        # print(b)
        #  
    # else:
        # b.append(i)
    # print(b)
    
# a=[1,2,3,[4,5,6,7,[8,9,10,[11,12,13]]]]
# b = []
# for i in a:
#     if type(i) == list:
#         for j in i :
#             b.append(j)
#     else:
#         b.append(i)
#         # print(i)
# print(b)
# a=[[14,[[13],[12,11,[18,20,]]],16,21]]

# while a:
#     b=a.pop()
#     if b==list:
#         a.extend(b)
#     else:
#         a.append(b)
# print(a)


# a=[[14,[[13],[12,11,[18,20,]]],16,21]]
# for i in range(len(a)):
    # for i in a:
        # if type(i)==list:
            # a.remove(i)
            # for j in i:
                # a.append(j)
# print(a)
# 

# a=[1,2,3,[4,5,[6,7,[8,9,10]]]]
# b=[]    
# for i in range(len(a)):
    # for i in a:
        # if type(i)==list:
            # a.remove(i)
            # for j in i:
                # b.append(j)
# print(b)
# print("""         *
        #  **
        #  ***
        #  ****
        #  *****""")

#date(recursion)
#(sum of numbers)
# def sum(n):
    # if n==1:
        # return 1
    # else:
        # return (n+sum(n-1))
# x=sum(4)
# print(x)

#(print reverse)
# def re(n):
    # if n==1:
        # print(1)
    # else:
        # print(n)
        # re(n-1)
# x=re(10)
# print(x)

#(string reverse)
# def rev(n,s):
    # if n==0:
        # print(s[0])
    # else:
        # print(s[n],end="")
        # rev(n-1,s)
# n1=input()
# x=rev((len(n1)-1),n1)
# print(x)

#(power ex xki power y)
# def pow(n,n1):
    # if n1==0:
        # return 1
    # else:
        # return (n*pow(n,(n1-1)))
# x=pow(2,3)
# print(x)

#(factorial)
# def fac(n):
    # if n==1:
        # return 1
    # else:
        # return (n*fac(n-1))
# n=int(input())
# x=fac(n)
# print(x)


#(fibonacci serise)
# a=0
# b=1
# z=1
# for a in range(1,11):
    # print(z)
    # a=b
    # b=z
    # z=a+b

# def fibo(i):
    # if i==0:
        # return 0
    # elif i==1:
        # return 1
    # else:
        # return (fibo(i-2)+fibo(i-1))
# for a in range(11):
    # x=fibo(a)
    # print(x)


#(w3resours q2)
# def sall(a):
    # c=0
    # for a1 in a:
        # c+=a1
    # return c
# 
# b=[3,6,8,0,3,1,3,6]
# x=sall(b)
# print(x)

#(w3resours q3)
# def sall(a):
    # c=1
    # for a1 in a:
        # c*=a1
    # return c
# 
# b=[8, 2, 3, -1, 7]
# x=sall(b)
# print(x)


#(w3resours 4. Write a Python program to reverse)
# def rev(a):
    # for b in range((len(a))+1):
        # if b!=0:
            # b=-b
            # print(a[b],end="")
# 
# a="1234abcd"
# rev(a)

#(5. Write a Python function)
# def fact(a):
    # c=1
    # for b in range(1,(a+1)):
        # c*=b
    # print(c)
# fact(3)

#(7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters)
# def cka(a):
    # caps=[chr(a1) for a1 in range(65,91)]
    # small=[chr(a1) for a1 in range(97,123)]
    # c=0
    # c1=0
    # for a3 in (a):
        # if a3 in caps:
            # c+=1
        # elif a3 in small:
            # c1+=1
    # print('cal',c)
    # print('small',c1)
# 
# cka('The quick Brow Fox')


#(8. Write a Python function that takes a list and returns a new list with unique elements of the first list.)
# def dub(a):
    # a1=[]
    # for a2 in a:
        # if a2 not in a1:
            # a1.append(a2)
    # print(a1)
# 
# a=[1,2,3,3,3,3,4,5]
# dub(a)

# def facb(n):
    # if n==0:
        # return 0
    # else:
        # return (facb(n-2)+facb(n-1))
# 
# x=facb(10)
# print(x)




# def pef(n):
    # c=0
    # for a in range(1,n):
        # if n%a==0:
            # c+=a
    # if c==n:
        # print('perfact number')
    # else:
        # print('not a perfact number',c)
# pef(6)

#(sum of eliment in recurtion)
# def suma(b):
    # a=len(b)
    # if a==0:
        # return 0
    # else:
        # return (a+suma(a-1))
# 
# b=[1,2,3,4,5,6,7,8,9,10]
# x=suma(b)
# print(x)

# print(b[1:])

# def listsum(a):
    # if len(a)==0:
        # return 0
    # else:
        # return (a[0]+listsum(a[1:]))
# 
# b=[1,2,3,4,5,6,7,8,9,10]
# x=listsum(b)
# print(x)


# a=[1,2,3,[4,5,[6,7,[8,9,10]]]]
# a=[[14,[[13],[12,11,[18,20,]]],16,21]]
# a=[1,2,3,4,[5,6,7,8]]
# c=[]
# b=len(a)
# b1=0
# while b1<=b:
    # if type(a[b1])==list:
        # a.extend(a[b1])
        # a.remove(a[b1])
        # b1=0
    # elif a[b1] not in c:
        # c.append(a[b1])
        # b1+=1
    # else:
        # b1+=1
# print(c)
# 
# if 2 in a:
    # a.remove(a[2])
    # a.append(a[2])
# print(a)

# def suma(a):
    





# 
# a=[1, 2, [3,4], [5,6]]
# print(suma(a))



# def recursive_list_sum(data_list):
	# total = 0
	# for element in data_list:
		# if type(element) == type([]):
			# total = total + recursive_list_sum(element)
		# else:
			# total = total + element
# 
	# return total
# 
# a=[[14,[[13],[12,11,[18,20,]]],16,21]]
# x=(recursive_list_sum(a))
# print(x)

#a=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15] #you should return [10, -65].

# fobj=open('/home/praveen/Desktop/bcb.txt','w')
# for a in range(10):
    # fobj.write(str(a)+/n)
# fobj.close()
# fobj=fobj=open('/home/praveen/Desktop/bcb.txt','r')
# x=fobj.read()
# print(x)

# def q(a,b):
    # if (a)==(b):
        # print()
        # return 
    # else:
        # print((a+1),end=" ")
        # q((a+1),b)  
# 
# def p(n):
    # global s
    # if n==0:
        # return 1
    # else:
        # p(n-1)
        # s=(s+n)
        # q((s-n),s)
# 
# s=0
# n=int(input())
# p(n)
# from cgitb import html
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(htm,"https://www.merakilearn.org/course/221/exercise/6565")
# print(soup.prettify)

# import requests,json
# from bs4 import BeautifulSoup
# uri='https://www.imdb.com/india/top-rated-indian-movies/'
# sp=requests.get(uri)
# print(sp)

# print(sp)
# htmlsp=sp.content
# print(htmlsp)
# souo=BeautifulSoup(htmlsp,'html peras')
# soup =souo.strip()
# a = json.dumps(souo.text)
# a=souo.text
# print(souo)
# print(souo.strip())

# with open('abhi2.json','w') as g:
#     # a=json.loads(a)
#     # print(type())
#     json.dump(souo.text,g,indent=4)



# def ler (m):
    # if m%2 ==0 and m>0:
        # print(10)
        # ler(m-1)
    # elif m%2 !=0:
        # print(11)
        # ler(m-1)
    # 
# ler(10)
# 
# def number(j):
    # if j == 1:
        # print(1)
    # else:
        # print(j)
        # number(j-1)
# 
# print('Welcome to our Dhaba')
# print("""
# pess 1 for Breackfast
# press 2 for Lunch
# press 3 for Dinner""")
# 
# Chhotu = int(input('which one you want'))
# 
# if Chhotu ==1:
    # print('\033[15m',"""
    # press 1 for Dall Rice
    # pess 2 for Rajma Rice
    # press 3 for Nonvage""",'\033[0m')
# 
    # ser1=int(input('which one you want'))
# 
    # print("""
    # press 1 for Half Plate
    # press 2 for Full Plate""")
    # ser2=int(input('which one you want'))
    # if ser2 ==1:
        # print("""price will be 100
        # come again!!""")
    # elif ser2==2:
        # rint("""price will be 200
        # come again!!""")
# 