#loops in python programming.
#there are several types of loops in python..
#1. for loop
#2. while loop 
#so let's see how to use them in python programming.
#for loop is used to iterate over a sequence.
#ex
for i in range(5):
    print(i) #output: 0,1,2,3,4
#here range() is function with 5 as argument which will generate a sequence of numbers from 0 to 4.
#range basically generates a sequence of numbers starting from 0 to the specified number -1.(in this case 5-1=4)
#also the format for range() function is range(start, stop, step).
#ex.
for i in range(1, 10, 2):
    print(i) #output: 1,3,5,7,9
#Questions on loops in python programming.
#sum of the numbers from 1 to 10 using for loop.
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of numbers from 1 to 10 is:", sum) #output: Sum of numbers from 1 to 10 is: 55
#sum of even numbers from 1 to 20 using for loop.
sum_even = 0
for i in range(2, 21, 2):
    sum_even += i
print("Sum of even numbers from 1 to 20 is:", sum_even) #output: Sum of even numbers from 1 to 20 is: 110
#sum of odd numbers from 1 to 20 using for loop.
sum_odd = 0
for i in range(1, 21, 2):
    sum_odd += i
print("Sum of odd numbers from 1 to 20 is:", sum_odd) #output: Sum of odd numbers from 1 to 20 is: 100  
#so this is basics of for loop in python programming.
#now, let's see how to use while loop in python programming.
#Questions on while loop in python programming.
#sum of the numbers from 1 to 10 using while loop.
sum = 0
i = 1
while i <= 10:  
    sum += i
    i += 1
print("Sum of numbers from 1 to 10 is:", sum) #output: Sum of numbers from 1 to 10 is: 55
#sum of even numbers from 1 to 20 using while loop.
sum_even = 0
i = 2
while i <= 20:
    sum_even += i
    i += 2
print("Sum of even numbers from 1 to 20 is:", sum_even) #output: Sum of even numbers from 1 to 20 is: 110
#sum of odd numbers from 1 to 20 using while loop.
sum_odd = 0
i = 1
while i <= 20:
    sum_odd += i
    i += 2
print("Sum of odd numbers from 1 to 20 is:", sum_odd) #output: Sum of odd numbers from 1 to 20 is: 100
#so this is basics of while loop in python programming.


#there is vast number of questions on loops in python programming.
#refer code and debug questions statements in python programming.
