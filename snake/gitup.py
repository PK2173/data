import json
def create():
    with open('t&p.json','r') as f1:
        r=json.load(f1)
    with open('t&p.json','w') as f:
        a1=int(input('enter your phone no'))
        a={
            'name':input('enter your name '),
            'email':input('enter ypur email'),
            'password':input('enter your password')
        }
        r[a1]=a
        json.dump(r,f,indent=4)
def remove():
    with open('t&p.json','r') as f1:
        r=json.load(f1)
    with open('t&p.json','w') as f:
        m1=int(input('enter your phone no'))
        del r[str(m1)]
        json.dump(r,f,indent=4)

def read():
    m1=int(input('enter your phone number'))
    with open('t&p.json','r') as f:
        fo=json.load(f)
        for a,b in (fo.items()):
            if a==str(m1):
                print(b)
                return 1

while True:
    print("""
    press 1 for read
    press 2 for create
    press 3 for Update
    press 4 for delete
    press 5 for exit
    """)
    m=int(input())
    if m==1:
        #m1=int(input('enter your phone number '))
        read()
    elif m==2:
        #m1=int(input('enter your phome number '))
        create()
    elif m==3:
        a=read()
        if a==1:
            create()
        else:
            print('not exist')
    elif m==4:
        remove()
    elif m==5:
        break
              
