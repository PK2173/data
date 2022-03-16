import csv


with open('/home/praveen/Desktop/details.csv','r') as fob:
    dob=csv.reader(fob)
    a1=[]
    for i in dob:
        a1.append(i[0])
with open('/home/praveen/Desktop/details.csv','a') as f1:
    dob1=csv.writer(f1)
    for i in range(1,6):
        a=int(input(''))
        b=int(input(''))
        c=int(input(''))
        d=[a,b,c]
        if str(d[0]) not in str(a1):
            dob1.writerow(d)
    
# 

