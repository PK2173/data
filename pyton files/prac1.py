# def chack(m1):
# m1=9599334028
# f=open("/home/praveen/Desktop/rec/curd/userdata",'r')
# value=" "
# c=0
# z=0
# while value:
    # if c%2==0:
        # value=f.readline()
        # print(value)
        # c+=1
        # if value==str(m1):
            # z=1
            # print('exist')
        # else:
            # c+=1
    # else:
        # c+=1
        # f.readline()
# if z==0:
    # creat(m1)
# else:
    # print('already exist')
# while value:
    # fabo=open("/home/praveen/Desktop/rec/curd/userdata",'r')
    # value=f.readline()
    # print(value)
    # print(len(value))
    # if str(m1) in value:
        # print('true')

# m='9599334028'
# n=9599334028
# if m==str(n):
    # print('true')

# n=int(input())
# b=int(input())
# try:
#     c=(n/b)
#     print(c)
# except Exception:
#     print("not valid")

# x = -1
# 
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# d={ 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# b=list(d)
# print(b)

# b=[1, 4, 9, 16, 25]
# c=5
# c1={}
# print(c1.fromkeys(b,c))
# 
# b1=[1, 2, 3, 4, 5]
# b=[1, 4, 9, 16, 25]
# c={}
# for a in range(5):
    # n=int(input())
    # n1=int(input())
    # c[n]=n1
# print(c)

# import json

# some JSON:
# x =  '{ "name":"John", "age":"30", "city":"New York"}'

# parse x:
# y = json.dumps(x)

# the result is a Python dictionary:
# print(y["age"])


# if False:
    # print("hello")
# else:        #colon will give us indentation whatever we want to take 1,2,3,4,5,21,32,43,5,545424321
#  print("i am currect")
    # print("i am ok or not")



############################CALL API AND CONVERT DATA INTO JSON FILE###############################

# import requests, json
# data = requests.get('http://saral.navgurukul.org/api/courses')
# a=data.json()
# print(type(a))
# with open('course.json','w') as f:
    # p=json.dump(a,f,indent=4)


# import requests, json
# data = requests.get('http://saral.navgurukul.org/api/courses')
# print(data)
# real_data = json.loads(data.text)
# with open('course-2.json','w') as f:
    # p=json.dump(real_data,f,indent=4) 
a="https://www.imdb.com//title/tt8176054/"
print(a[28:-1]+'.json')