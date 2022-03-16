import random
a=[ '.what is my name?',
    '.who is prasident of india?',
    '.what is capital of india?',
    " .How many continents in the world?",
    " .Which day is observed as the world standard day?",
    " .what is the national food of Navgurukul?",
    " .Who is the author of the epic 'Magdoot'?",
    " .September 27 is celebrated every year as?",
    " .How many planets are there in our solar system?",
    " .Who is the president of America?",
    " .where is nasa"]
# 
# 
b=[ ['1=praveen','2=anikat','3=akash','4=ranveer','5=Life line'],
    ['1=Modi','2=ramnath govind','3=akhilash','4=lalu','5=Life line'],
    ['1=Bihar','2=Rajesthan','3=Delhi','4=Gujrat','5=Life line'],
    ["1=1","2=5","3=4","4=7","5=Life line"],
    ["1=June 26","2=Oct 14","3=Nov 15","4=Dec 2","5=Life line"],
    ["1=Rice","2=Fried","3=Fried Rice","4=Dal","5=Life line"],
    ["1=Vamlmiki","2=Banabhata","3=Kalidas","4=Vishal","5=Life line"],
    ["1=Teacher,s Day","2=Natinal Integretion Day","3=World Tourism Day","4=International Day","5=Life line"],
    ["1=5","2=8","3=9","4=6","5=Life line"],
    ["1=Joe Biden","2=Donald Trump","3=Emmanuel Macron","4=Barack Obama","5=Life line"],
    ['1).Washington, D.C.','2). California ','3).Colorado','4).Connecticut']]
e=[]
j=[['1).Praveen','2).Anikat'],
   ['2).Ramnath Govind','3).Akhilash'],
   ['1).Bihar','3).Delhi'],
   ['1.)1','4).7'],
   ['1).June 26','2).Oct 14'],
   ['4).Dal','3).Fried Rice'],
   ['2).Banabhata','3).Kalidas'],
   ['4).International Day','3).World Tourism Day'],
   ['2)8','4).6'],
   ['1).Joe Biden','2).Donald']]
life=['1).50:50','2).Phone-a-Friend','3).Audience Poll','4).Switch the Question']
life1=0
life2=0
life3=0
life4=0
y=0
ad0=1
while ad0>0:
    ad=random.randint(1,101)
    ad1=random.randint(1,101)
    ad2=random.randint(1,101)
    ad3=random.randint(1,101)
    if ad+ad1+ad2+ad3==100:
        break
    else:
        ad0+=1
g=[1,2,3,4,2,3,3,3,2,1,1]
guss=[0,1,2,3,4,5,6,7,8,9,10]
e=[]
h=200
cs=0
while cs<=10:
    cs+=1
    c=random.choice(guss)
    print('This Qustion for',h,'Amount')
    print('Q-',cs,'\033[1m','\033[91m',a[c],'\033[0m')
    print()
    guss.remove(c)
    for i in range(5):
        print('\033[94m',b[c][i],'\033[0m')
    print('\033[10m','Enter your answer','\033[0m')
    k=int(input())
    if k==5:
        if life1==1:
            print()
            print('\33[37m','already uesed 50:50','\33[0m')
        if life2==1:
            print('\33[37m','already uesed Phone a friend','\33[0m')
        if life3==1:
            print('\33[37m','already uesed Audience Poll','\33[0m')
        if life4==1:
            print('\33[37m','already uesed Switch the Question''\33[0m')
            print()
        for li in (life):
            print('\33[33m',li,'\33[0m')
        print()
        print('choice any option')
        lif=int(input())
        if lif==1 and life1<1:
            print('Correct Answear is ')
            for opp in (j[c]):
                print(opp)
            print()
            print('\033[10m','Enter your answer','\033[0m')
            l=int(input())
            e.append(l)
            life.remove('1).50:50')
            life1+=1
        elif lif==2 and life2<2:
            print('correct Answear',g[c])
            print()
            print('\033[10m','Enter your answer','\033[0m')
            l=int(input())
            e.append(l)
            life.remove('2).Phone-a-Friend')
            life2+=1
        elif lif==3 and life3<1:
            if ad+ad1+ad2+ad3==100:
                print('Audience',ad,'% =>1). option')
                print('Audience',ad1,'% =>2). option')
                print('Audience',ad2,'% =>3). option')
                print('Audience',ad3,'% =>4). option')
            print()
            print('\033[10m','Enter your answer','\033[0m')
            l=int(input())
            e.append(l)
            life.remove('3).Audience Poll')
            life3+=1
        elif lif==4 and life4<1:
            c=10
            print('correct Answer',g[c])
            l=g[c]
            print('Switch')
            print(a[c])
            for a1 in (b[c]):
                print(a1)
            print()
            print('\033[10m','Enter your answer','\033[0m')
            l=int(input())
            e.append(l)
            life.remove('4).Switch the Question')
            life4+=1
        y+=1
        if l==g[c]:
            h+=h*2
            print('\33[5m','you won',h,'rs','\33[0m')
            print()
            print('\033[1m','Next Qustion is','\033[0m')
        else:
            print('\33[5m','you lose','\33[0m')
            print('Do you want play continu enter y or n')
            gk=input()
            if gk=='y':
                cs=0
            else:
                break
    elif k==5 and y==1:
        print('already used our Life line')
        l=int(input())
        e.append(l)
        if l==g[c]:
            h+=h*2
            print('\33[5m','you won Total',h,' rs','\33[0m')
            print()
            print('\033[1m','Next Qustion is','\033[0m')
        else:
            print('\33[5m','you lose','\33[0m')
            print('Do you want play continu enter y or n')
            gk=input()
            if gk=='y':
                cs=0
            else:
                break
    else:
        l=k
        e.append(k)
        if l==g[c]:
            h+=h*2
            print('\33[5m''you won Total ',h,'rs','\33[0m')
            print()
            print('\33[1m','Next Qustion is','\33[0m')
        else:
            print('\33[5m','you lose','\33[0m')
            print('Do you want play continu enter y or n')
            gk=input()
            if gk=='y':
                cs=0
            else:
                break
print('Your Answear')
print('Won Amount',h)
# 
# (date/4-2-22) gassing game
# import random
# print('Wecome to gassing game')
# for a in range(1,6):
    # b=random. randrange(1,11)
    # print('Enter your gass no')
    # c=int(input())
    # if b==c:
        # print('congratulations you won')
        # break
    # elif b>=c:
        # print('gass number is greater than your no')
        # print()
        # if a+1==5:
            # print('Last chance')
        # else:
            # print(a+1,'chance try again')
    # elif b<=c:
        # print('gass number is less then your no')
        # print()
        # if a+1==5:
            # print('Last chance')
        # elif a+1==6:
            # print('Game Over')
        # else:
            # print(a+1,'chance try again')
    #   
# (stone paper scissors)
# import random
# d=['stone','paper','scissors']
# print('Welcome')
# print('Rock paper scissors Game')
# for a in range(1,4):
    # b=random. randint(0,3)
    # print()
    # print('press 0 for stone')
    # print('press 1 for paper')
    # print('press 2 for scissors')
    # n=int(input())
    # if n==b:
        # print('Match Draw')
    # elif (n==0 and b==1) or (n==1 and b==2) or (n==2 and b==0):
        # print(d[b])
        # print('you loss')
        # print('try again')
        # print()
    # elif (n==0 and b==2) or (n==1 and b==0) or (n==2 and b==1):
        # print(d[b])
        # print('congratulations you won')
        # break
    # else:
        # print('Enter valid number')
# b=random. randint(1,4)
# print(a[b])

# d={1:11,2:22,3:33,4:44}
# d.update({1:12})
# print(d)

# def  meal(day,time):
    # if day=="sunday":
    #  if time=="breakfast":
    #   return "dosa"
    #  elif time=="lunch":
    #   return "dal rice"
    # elif time=="dinner":
        # return "paneer and  chapati"
    # else :
        # return "time not found"
    # elif day=="monday":
    # if time=="breakfast":
        # return "fried rice"
    # elif time=="lunch":
        # return "aloo rice"
    # elif time=="dinner":
        # return "chhole bhature"
    # else :
        # return "time not found"
    # elif day=="other":
    # if time=="breakfast":
        # return "aloo"
    # elif time=="lunch":
        # return "rajma rice"
    # elif time=="dinner":
        # return "veg-chapati"
    # else :
        # return "time not found"
    # 
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

# print(ord('A'))

