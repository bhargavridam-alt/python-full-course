# strings are also immutable and iteratable
# a = "ridam"
# a[3] = "x" #strings are immutable i.e it's an error.
# print(a)
# a = "bhargav"
# # print(a[2])
# for i in a:
#     print(i)

# string operations and ascii codes values
# the supported operations for strings are +,*.
# a = "ridam"
# print(a*3) output: ridamridamridam
# b = "bhargav"
# print(a+b) output: ridambhargav
# conditional operators.
# a = "ansh"
# b = "Ansh"
# print(a>b) output : True
# print(a<b) output : False
# here we will see the ascii value role.
# everything on ur keyboard has a ascii value
# "a" = 97
# "A" = 65
# we can find this using ord and chr.
# print(ord("A")) #output: 65 
# print(chr(97)) output : a

# string slicing
# similar as in the list slicing.
# a = "ridam bhargav"
# print(a[6:]) #output: bhargav

# string methods 
# there's a lot of string methods but some of imp are given below.
# x = "dsa iS hard"
# print(x.title()) #capitalise the first letter of each word and makes all other letters lowercase
# print(x.capitalize())#capitalise only first letter of word and makes all other letters lowercase
# print(x.casefold())
# print(x.center()) 
# print(x.count()) #returns the no. of occurence of the argument in the string.
# print(x.encode())
# print(x.endswith()) #returns bool for the argument (true or false.)
# print(x.expandtabs())
# print(x.find())# same as index just do not give error when asked non existing cha. instead gives -1.
# print(x.format())
# print(x.format_map())
# print(x.index()) #used to get the first index of a character in a string.
# print(x.isalnum()) #True if everything is alphabet or number else false
# print(x.isalpha()) #true, everything is alphabet. Else false.
# print(x.isascii())
# print(x.isdecimal())
# print(x.isdigit()) #true, if everything is number else false
# print(x.isidentifier())
# print(x.islower()) #true, if everything is lowercase, else false.
# print(x.isnumeric())
# print(x.isprintable())
# print(x.isspace()) #\n or \t or empty space, then true, else false.
# print(x.istitle())
# print(x.isupper()) #returns boolean true if everything is uppercase, else false.
# print(x.ljust)
# print(x.lower) #change all letters to lowercase.
# print(x.lstrip)
# print(x.maketrans)
# print(x.partition)
# print(x.removeprefix)
# print(x.removesuffix)
# print(x.replace())# creates a new string with replaced chracter. syntax x.replace("original","replaced").
# print(x.rfind)
# print(x.rindex)
# print(x.rjust)
# print(x.rpartition)
# print(x.rsplit)
# print(x.rstrip)
# print(x.splitlines)
# print(x.startswith())# returns bool for the argument (true or false.)
# print(x.strip())# by default, the argu is space actually it removes the spaces there are in starting as well in ending and if i give any argument and then the string is starting or ending with that argument then it will also remove that.
# print(x.swapcase) #change upper to lower and lower to upper and vice versa.
# print(x.translate)
# print(x.upper) # change all letters to uppercase.
# print(x.zfill)

# split and join.
# split breaks the string from whatever argument is given. and returns a output of list.
# print(x.split()) #by default it is a space.
# output: ['dsa','is','hard']
# if we have to break x = r+i+d+a+m then,
# x = "r+i+d+a+m"
# print(x.split("+"))
# output: ['r', 'i', 'd', 'a', 'm']
# similarly, the syntax of join is :
# a = x.split("+")
# print("".join(a)) output: ridam
# **********note: joining is only used on strings and can't be used in any other data type.
# if there's sudden need of joining other data type from list as well then list comprehension can be used.
# a = [12,21,"dfdwe","dwq",3921]
# print(" ".join(str(i) for i in a ))
# output:12 21 dfdwe dwq 3921


