# (curd qustion)
# # userDetails = {}
# # while True:
#     # print("""
#     # press 1 for update
#     # press 2 for delete
#     # press 3 for read
#     # press 4 for create
#     # press 5 for exit
# # 
#     # """)
#     # n=int(input('Enter your option: '))
#     # if n==1:
#         # n1=int(input('enter your phone no'))
#         # if n1 in userDetails:
#             # userDetails.update({(n1):{
#             # 'name':input("enter name"), 
#             # 'email':input("enter email"),
#             # 'password':input("enter password"),
#         # }})
#     # elif n==2:
#         # userDetails.pop(int(input('enter your phone no')))
#     # elif n==3:
#         # print(userDetails[int(input('enter your phone no'))])
#     # elif n==4:
#         # n2=int(input('enter your phone no'))
#         # if n2 in userDetails:
#             # print('already exist')
#         # else:
#             # userDetails[n2]=({
#                 # 'name':input("enter name"), 
#                 # 'email':input("enter email"),
#                 # 'password':input("enter password"),
#             # })
#     # elif n==5:
#         # exit()
#     # else:
#         # print('Not Valid')
# def chack(m1):
#     f=open("/home/praveen/Desktop/rec/curd/userdata",'r')
#     value=" "
#     c=0
#     z=0
#     while value:
#         if c%2==0:
#             value=f.readline()
#             if str(m1) in value:
#                 z=1
#             else:
#                 c+=1
#         else:
#             c+=1
#             f.readline()
#     if z==0:
#         creat(m1)
#     else:
#         print('already exist')

# def creat(m1):
    # f=open("/home/praveen/Desktop/rec/curd/userdata",'r')
    # s=f.read()
    # if str(m1) in s:
        # print('alraedy exist')
    # else:
        # user_data=open("/home/praveen/Desktop/rec/curd/userdata",'a')
        # n=input('enter uour email ')
        # value=user_data.write(str(m1))
        # value=user_data.write('\n')
        # value=user_data.write(n)
        # value=user_data.write('\n')
        # user_data.close()
        # print('succesful')
# 
# def read(m1):
    # user_data=open("/home/praveen/Desktop/rec/curd/userdata",'r')
    # c=0
    # value=" "
    # while value:
        # value=user_data.readline()
        # if str(m1) in value:
            # print(value)
            # print('This is your email')
            # print(user_data.readline())
            # c+=1
    # if c==0:
        # print("not exist try again")
    # user_data.close()
# 
# while True:
    # print("""
    # press 1 for read
    # press 2 for create
    # press 3 for exit
    # """)
    # m=int(input())
    # if m==2:
        # m1=int(input('enter your phone number '))
        # creat(m1)
    # elif m==1:
        # m1=int(input('enter your phome number '))
        # read(m1)
        # if m1 not in contact_list:
            # print('not exist try again')
        # else:
            # read(m1)
    # elif m==2:
    #     m1=int(input('enter ypur phone number '))
    # elif m==1:
    #     m1=int(input('enter your phone number '))
    #         # m1=int(input('enter your phone number '))
    #         # contact_list.append(m1)
    #     creat(m1)
    #     # else:
    #         # print('not exist try again')
    # elif m==3:
        # break
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# b=sorted(a.items(),key=lambda t:t [1] ,reverse=True)
# print(b)
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

# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }

# details=open('/home/praveen/Desktop/rec/pk1','w')
  
# json.dump(dict1,details,indent = 8)
  
# details.close()

# details=open('/home/praveen/Desktop/rec/pk1','r')
# a=json.load(details)
# print(a['emp1'])



import json, os
def creat():
    
    if os.path.exists('pk1.json'):
        with open("pk1.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    a1={
        "name":input('Enter your Name'),
        "Phone no":int(input('Enter your Phone')),
        "email":input('Enter your Email')
    }
    data.append(a1)
    with open('pk1.json', "w") as f:
        json.dump(data, f, indent=4)
    

def read(m1):
    with open("pk1.json", "r") as f:
        data = json.load(f)
    for entry in data:
        if entry['Phone no'] == m1:
            print(entry)
            return
    else:
        print('Not exist')

def update(m1):
    with open("pk1.json", "r") as f:
        fo=json.load(f)
        for a in fo:
            # for i in (a.items()):
                # print(i)
            if m1==(a['Phone no']):
                print(a)
def remove(a):
    with open("pk1.json", "w") as f:
        fo=json.dump(f)

while True:
   print("""
   press 1 for read
   press 2 for create
   press 4 for Update
   press 3 for exit
   """)
   m=int(input())
   if m==2:
    #    m1=int(input('enter your phone number '))
       creat()
   elif m==1:
       m1=int(input('enter your phome number '))
       read(m1)
   elif m==4:
       m1=int(input('Enter your phone no'))
       update(m1)
   elif m==3:
       break
# 