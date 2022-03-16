# import json, os
# def creat():
    # 
    # # if os.path.exists('pk1.json'):
        # with open("pk1.json", "r") as f:
            # data = json.load(f)
    # else:
    #     # data = []
    # a={
    #     # "name":input('Enter your Name'),
        # "Phone no":int(input('Enter your Phone')),
        # "email":input('Enter your Email')
    # }
    # # data.append(a)
    # with open('pk1.json', "w") as f:
        # json.dump(data, f, indent=4)
    
    
# # 
# # def read(m1):
#     # if not os.path.exists('pk1.json'):
        # return "Not Exist"
    # with open("pk1.json", "r") as f:
        # data = json.load(f)
# # 
#     # with open("pk1.json", "r") as f:
        # data = json.load(f)
    # for entry in data:
        # if entry['Phone no'] == m1:
            # print(entry)
            # return
        # else:
        #     print('Not exist')
    
# 
# # while True:
# #    print("""
# #    press 1 for read
#    press 2 for create
#    press 3 for exit
#    """)
# #    m=int(input())
#    if m==2:
#        m1=int(input('enter your phone number '))
#        creat()
# #    elif m==1:
#     #    m1=int(input('enter your phome number '))
#        read(m1)
# #    elif m==3:
# #        break
# 

# import requests, json
# url=requests.get('http://saral.navgurukul.org/api/courses')
# reps=requests.get(url)
# print(reps)
# a=reps.json()
# print(type(a))
# with open ('abhi.json','w') as f:
#     json.dump(a,f,indent=4)

