# from flatifylists import flatifyList
# 
# example = [[[1,2], [3,[4,[5],6],7],8,9]]
# 
# print(flatifyList(example))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a=[1,2,3,[4,5,[6,7,[8,9,10]]]]
# print(f)

# from functools import reduce
# from operator import concat
# 
# nestedlist = [1,2,3,[4,5,[6,7,[8,9,10]]]]
# flatlist = reduce(concat, nestedlist)
# print(flatlist)
# 
# pip install flatifylists

# import flatten_list

# fobj= open(r'/home/praveen/Desktop/bcb.txt','r')
# a=fobj.readlines()
# print(a)
# fobj.close()
a='miirepss'
b=[]
for i in a:
    # print(i)
    b.append(i)
n1=input()
n=b.index(n1)
b.remove(b[n-1])
v=" "
for e in b:
    v+=e
print(v)

