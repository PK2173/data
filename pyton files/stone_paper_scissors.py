# (stone paper scissors)
import random
d=['stone','paper','scissors']
print('Welcome')
print('Rock paper scissors Game')
for a in range(1,4):
    b=random. randint(0,3)
    print()
    print('press 0 for stone')
    print('press 1 for paper')
    print('press 2 for scissors')
    n=int(input())
    if n==b:
        print('Match Draw')
    elif (n==0 and b==1) or (n==1 and b==2) or (n==2 and b==0):
        print(d[b])
        print('you loss')
        print('try again')
        print()
    elif (n==0 and b==2) or (n==1 and b==0) or (n==2 and b==1):
        print(d[b])
        print('congratulations you won')
        break
    else:
        print('Enter valid number')
b=random. randint(1,4)
print(a[b])