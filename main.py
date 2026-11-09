# dict = {"name": "Ridam","old": 24,"new": 1.0}
# for key in dict:
#     value=dict[key]
#     print(key,value)

# print(dict.items()) # [('name', 'Ridam'), ('old', 24), ('new', 1.0)]

# s="asdfghjkrtecuwasgdfjsgjsjdfjags"
# hash={}
# for i in range(len(s)):
#     hash[s[i]] = hash.get(s[i],0) + 1
# print(hash)


#list

# arr=[67,14,13,4]
# arr2=[4,8,9]
# arr.append(2) # adds to last
# arr.pop() # removes last element O(1) 
# arr.extend(arr2)

# arr3=arr[:]
# arr4 = arr.copy()
# arr[0]=1111
# print(arr)
# print(arr3)

# copy creates a new list and arr3 is not affected by changes in arr.

# print(arr[-1])
# for i in range(len(arr)):
#     print(arr[i])

# print(arr[::-1])



# Tuple (immutables)

# tup = (1,2,2,4)
# print(tup.count(2))
# print(tup.index(2))

# print(tuple(arr))


# strings

# s = "  asDfgh ghjsd "
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.find("k")) # prints -1 if doesnt exist ... and index of first occ if exists
# print(s.replace("asD","hello"))
# print(s.startswith("asD"))
# print(s.endswith("sd"))
# print(s.count("s"))

# print(s.split(" "))
# print("-".join(map(str,tup)))
# print(s.partition("g")) # ('asDf', 'g', 'h ghjsd')
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# a="range"
# b="bhargav"
# print(a.center(20))
# print(b.center(20))
# print(a.zfill(10))
# print(a.isalpha())
# print(a.isdigit())
# print(a.isalnum())
# print(a.isspace())
# print(a.islower())
# print(a.isupper())
# print(a.isidentifier())


# a = input().split()
# b = list(map(int,a))
# print(a,b)
# a,b=map(int,input().split())
# arr=list(map(int,input().split()))
# print(arr)



# i=1
# while i%5!=0:
#     print(i)
#     i+=1

# i=0
# while i<=5:
#     # if i==1:
#     #     continue
#     # if i==2:
#     #     pass
#     if i==3:
#         break
#     i+=1
#     print(i)

# for i in range(5):
#     j=0
#     while j<=i:
#         print(j)
#         j+=1

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")

# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))   

# arr = [i*2 for i in range(5)]
# arr=[0]*5
# print(arr)

# print(ord("#"))
# print(chr(35))

# print("aA">"aa")

# arr=[[2,3],[4,5]]

# for u,v in arr:
#     print(u,v)
# arr1=[1,3,4,5]
# arr2=[1,2,4,4,8]
# for i,j in zip(arr1,arr2):
#     print(i,j)

# destructuring - arr, obj

# [a,b,*c]=arr1
# print(a,b,c)

# obj = {
#     "name":"Ridam",
#     "age":18
# }
# name=obj["name"]
# print(name)

# a = set([1,2,2,3,4])
# b=set([1,8])
# a.add(5)
# a.pop()
# a=a.union(b)
# print(a)

# s=set()
# a="1234567rsdfggbxfncgcgvhgzdfbfdsasdsdfdazvcxb"
# for i in a:
#     s.add(i)
# print(list(s))

#try except , err handling

# try:
#     # a=2/0
#     # print(a)
#     arr=[1,2]
#     print(arr[3])
# except ZeroDivisionError:
#     print("zero div")
# except IndexError:
#     print("nope")
# except:
#     print("smthin")
# finally:
#     print("finally block")


# file handling
# a=append,r=read,w=write
# f=open("hello.txt","a")
# print(f.write("hello world\ntest"))
# print(f.write("\nappend"))
# print(f.truncate())
# print(f.readlines(1))


# funcs

# def func(a,b,c):
#     return 1

# func(a=1,b=2,c=3) #named params
# func(1,2,3) #positional params

# args and **kwargs (keyword args)
# def func(a,b,*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,4,5,name="Ridam",age=18)

# global scope and local scope

# global_var = 10
# def func():
#     global_var = 20
#     return global_var
# print(func(),global_var)


#print 1 to n via rec
# n=5
# def rec(num):
#     if num>n:
#         return
#     rec(num+1)
#     print(num)
# rec(1)

#fibbb by rec
# n = 32

# def fibb(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibb(n-1)+fibb(n-2)
# for i in range(n):
#     print(fibb(i), end = ' ')


# palindrome
# def pal(n):