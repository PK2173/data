import requests, json
url='http://saral.navgurukul.org/api/courses'
rep=requests.get(url)
b=rep.json()
with open('abhi.json','w') as a:
    json.dump(b,a,indent=4)
with open('abhi.json','r') as f:
    a=json.load(f)
    a1=[]
    b1=1
    for q,w in (a.items()):
        for t in w:
            print(b1,t["name"])
            b1+=1
            a1.append(t["id"],)

n=int(input('enter wich one you want'))
sp=requests.get(f'http://saral.navgurukul.org/api/courses/{a1[n-1]}/exercises')
v=sp.json()
with open('abhi1.json','w') as a:
    json.dump(v,a,indent=4)
with open('abhi1.json','r') as b:
    b2=json.load(b)
    c1=1
    c2=[]
    for a,c in (b2.items()):
        for t in c:
            print(c1,t["slug"])
            c1+=1
            c2.append(t["id"])

n1=int(input('enter wich one you want'))
sp=requests.get(f'http://saral.navgurukul.org/api/courses/{c2[n1-1]}/exercises')
v1=sp.json()
with open('abhi2.json','w') as a:
    json.dump(v1,a,indent=4)
with open('abhi2.json','r') as b:
    b3=json.load(b)
    print(b3)