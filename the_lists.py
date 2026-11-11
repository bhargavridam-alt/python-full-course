# lists are mutable and iteratable.
# a is the list
a = ["ridam","ansh",44,66.6,False]
print(a) #output: ['ridam', 'ansh', 44, 66.6, False]
# iterate by value
for i in a:
    print(i,end = " ") #output: ridam, ansh, 44, 66.6, False
# # iterate by index
for i in range(len(a)):
    print(a[i],end = " ") #output: ridam, ansh, 44, 66.6, False
# list methods
# append: appends value to the last of the list.
a = [1,4,6,8,15]
a.append(10)
a.append(4)
print(a) # output: 1,4,6,8,15

# insert: adds any data type to any position. if the index is out of range than the element get added to the last.
a = [1,"good",9,16]
a.insert(3,"ridam")
print(a)#[1, 'good', 9, 'ridam', 16]

#updating value of the list.
a= [1,6,7,23,65,86,210]
a[2]= 44 #if i assign a = 100 then the output will be 100.coz i overwrite this.
print(a) #output: [1, 6, 44, 23, 65, 86, 210]

#pop
# by default removes the last one.
# else removes the indexed one.
a = [12,32,54,76,243,564]
a.pop(2) 
print(a) #output: [12, 32, 76, 243, 564]

# remove
# similar as pop but removes by value
a= ["ridam","rupali",44, "ridam", "shark", 431,987]
a.remove("ridam")
print(a) #output: ['rupali', 44,'ridam', ' shark', 431, 987]

#del
#delete by index
a = [32,432,5456,6754,"or"]
del a[4]
print(a)

# clear
a = [1209,1233,43546,5676865]
a.clear()
print(a) #output: []

# index : to give the index of the element/value.
a = [32,"ridam",290,True, 293]
b = a.index(290)
print(b) #output: 2
 
# sort
a = [12,6,23,43,54,2,21,45]
a.sort() #arrnge in ascending order respective of data types.
print(a) #output: [2, 6, 12, 21, 23, 43, 45, 54]
# **************note we can use it in a way like a.sort(reverse=True),it will descend the order.
# reverse
a = ["ridam","ansh",44,66.6,False]
a.reverse() #reverses the list irrespective of data types
print(a) #output: [False, 66.6, 44, 'ansh', 'ridam']

# extend 
# extend is basically a list method to elaborate the list in a list.
a = [3,2,"ridam","rupali",True]
a.extend([24,37,"rupali",False,783])
print(a)# output : [3, 2, 'ridam', 'rupali', True, 24, 37, 'rupali', False, 783]

# count : tells the no. of occurence of the element in the list.
a = [12,25,"for",45,25,36,76,43,25]
r = a.count(25)
print(r) #output : 3

# copy
# copy the whole list in the second list that is getting two diff addresses not pointing both variables towards a same address.
a = [12,23,423,543646,5765,87768]
b = a.copy()
a[3] = 100
print(b)

# membership operator.
# they are basically the true and false telling if a element exists in a list.
a = ["ridam","ansh",44,66.6,False]
x = input()
if x in a:
    print("Yes")
else:
    print("No")
# this can be replaced by the a.count>0 if yes then the element exists.

# list comprehension.
# to create a list of large range we use this one .
a = [i for i in range(1,21)] #here the i can be any expression.
print(a) #output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# here we can also use ternary opeator.
a = ["even" if i%2==0 else "odd" for i in range(1,21)]
print(a)
# to print all even numbers.
a = [i for i in range(1,31) if i%2==0]
print(a)

# list slicing.
a = ["ridam","bhargav",243,True,3901,3123,574,754]
# # slicing the list of a and putting the desired element in b.
b = a[0:9:2]
print(b) #output: ['ridam', 243, 3901, 574]
a = ["ridam","bhargav",243,True,3901,3123,574,754]
# # slicing in negative start stop or step.
b = a[::-1]
print(b)
