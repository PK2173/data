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
# example = [[[1,2], [3,[4,[5],6],7],8,9]] 
# print(flatten_list(example))


# from romanalphabet.romanalphabet import RomanAlphabet
# rr = RomanAlphabet("4785")
# rr.convert_to_roman()
# 'MMMMDCCLXXXV'


#(Roman Number)
# roman_dict={ 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
# num=int(input("enter a int num:"))
# int_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# for i in int_num:
    # if num!=0:
        # quo=num//i
        # if quo!=0:
            # for j in range(quo):
                # print(roman_dict[i],end="")
        # num%=i


#(flaten list)
# -1
# -12
# -123
# -1234
# -12345   # input 5


# def s(n):
    # if n==1:
        # print(1)
    # else:
        # s(n-1)
        # print(int(n)*str(n))
# 
# s(5)

# def s(n):
    # if n==1:
        # print(1)
    # else:
        # s(n-1)
        # p

# def s(a):
    # if a==0:
        # print(1)
    # else:
        # print(str(a)+str(s(a-1)))
# 
# s(5)

#(patter p)
# def s(a):
    # if a==0:
        # print()
        # return 0
    # else:
        # s(a-1)
        # print(a,end=" ")
# 
# def r(n):
    # if n==0:
        # return 0
    # else:
        # r(n-1)
        # s(n)
# 
# r(5)

# def s(a):
    # if a==0:
        # print()
        # return 0
    # else:
        # s(a-1)
        # print(a,end=" ")
# 
# s(5)
#(""
# 1
# 23
# 456
# 78910
# """)

# def s(a,b):
    # if a==b:
        # print()
        # return 
    # else:
        # print(a,end=" ")
        # s((a+1),b)  
# s(1,10)

#(code war)
#(Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.
# 
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
# def count_positives_sum_negatives(arr):
    # c=0
    # c1=0
    # if len(arr)>0:
        # for a in arr:
            # if a<0:
                # c+=a
            # elif a==0:
                # c1+=0
            # else:
                # c1+=a/a
        # return [c1,c]
    # else:
        # return []
# 
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# x=count_positives_sum_negatives(a)
# print(x)



#(Factorial decomposition)
# def decomp(n):
# 
    # number_count = {2 : 1}
    # return_str = ""
# 
    # def add_list(num):
        # if num not in number_count:
            # number_count[num] = 1
        # else:
            # number_count[num] += 1
# 
    # for x in range(n, 1, -1):
        # add = False
        # for y in range(1, x):
            # if x == 1 or y == 1: continue
            # a = True
            # while a:
                # if x % y == 0 and y != 1:
                    # x = int(x / y)
                    # add_list(y)
                # else:
                    # a = False
                    # add = True
# 
        # if add and x != 1:
            # add_list(x)
# 
    # number_count3 = {k: number_count[k] for k in sorted(number_count.keys())}
# 
    # for x, y in number_count3.items():
        # if y == 1:
            # return_str += str(x) + " * "
        # else:
            # return_str += str(x) + "^" + str(y) + " * "
# 
    # return return_str[:-3]
# 
# 
# x=decomp(12)
# print(x)
# 
#    or
# 
# 
# 
# def decomp(n):
    # f = {}
    # for  i in range(2, n+1):
        # for j in range(2, int(i**0.5)+1):
            # while i%j==0:
                # i = i//j
                # if j in f: f[j] += 1
                # else: f[j] = 1
        # if i!=1:
            # else: f[i] = 1
        # 
    # return ' * '.join(["{}^{}".frmat(i, f[i]) if f[i]>1 else str(i) for i in sorted(f)])

# def sum(k):
    # a=0
    # while a<0:
        # print(k)
        # a+=1
# sum('')

# import time
# for i in range(11):
    # print(i)
    # time.sleep(2)