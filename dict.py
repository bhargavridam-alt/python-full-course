# dict is all about keywords and value.
# syntax key: value under {} bracket
# key and value can be of any data type.
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
# }
# print(x)
# what if i add a same key with distinct value.
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
#     "name" : "ansh",
# }
# print(x)
#output: {'name': 'ansh', 'age': 18, 'marks': 99.9, 'subject': 'dictionary'}
# that is the key got updated.

# there's no position inside the dictionary i.e no index.
# get,add,Update,remove.
# # here we have to give key instead of index 
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
#     "name" : "ansh",
# }
# print(x["name"]) #output: ansh
# # similarly get can be used as 
# print(x.get("name")) #output: ansh

# if we have to take input
# n = input()
# if n is None:
#     print("not exists")
# else:
#     print(x.get(n))

# updating values of the dictionary.
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
# }
# x["age"] = 19
# x["name"] = "ansh"
# print(x.get("name"),end = " ")
# print(x.get("age"))
# # ouput: ansh 19
# if we give non existing key to update the value then it can create a new key with that value. 

# using .update to add and update multiple lists.
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
# }
# x.update({"age":19,"name":"ansh","address":"Delhi"})
# print(x)  

# del is a universal function to del or remove smthin'
# in dict we use them like
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
# }
# del x["name"]
# print(x) #{'age': 18, 'marks': 99.9, 'subject': 'dictionary'}
# del x
# print(x) #error x is not defined.
# also, can be removed by pop.
# x.pop("name")

# printing seprate keys and values specifically.
# x = {
#     "name" : "ridam",
#     "age" : 18,
#     "marks" : 99.9,
#     "subject" : "dictionary",
# }
# for i in x:
#     print(i) #here we are printing keys.
#     print(x[i]) #here we are printing values.its syntax is little bit like indexes.
# also we can print values by .values()
x = {
    "name" : "ridam",
    "age" : 18,
    "marks" : 99.9,
    "subject" : "dictionary",
}
# for i in x.values():
#     print(i)
# # for keys similarly,
# for i in x.keys():
#     print(i)
# # now, remember items that can do theh work both of these.
# for i,j in x.items():
#     print(i)
#     print(j)
# here the first one that is i denotes the keys and sec one denotes the values.
