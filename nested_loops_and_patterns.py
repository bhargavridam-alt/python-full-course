'''lets start with nested loops and patterns in python programming.'''
#nested loops are loops inside loops in python programming.
#ex. 
for i in range(5):
    for j in range(5):
        print(i, j) #output: 0 0, 0 1, 0 2, 0 3, 0 4, 1 0, 1 1, 1 2, 1 3, 1 4, 2 0, 2 1, 2 2, 2 3, 2 4, 3 0, 3 1, 3 2, 3 3, 3 4, 4 0, 4 1, 4 2, 4 3, 4 4
#here, the outer loop will run 5 times and for each iteration of the outer loop, the inner loop will run 5 times. so the total number of iterations will be 5*5=25.
#so this is basics of nested loops in python programming.
# now let's see how to use nested loops to print patterns in python programming.
# questions on patterns in python programming.
#1. print a square pattern of * using nested loops in python programming.
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print() 
    #output: * * * * *, 
    #        * * * * *, 
    #        * * * * *, 
    #        * * * * *, 
    #        * * * * *
#2. print a right angled triangle pattern of * using nested loops in python programming.
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print() #output: *,
                #    * *,
                #    * * *,
                #    * * * *, 
                #    * * * * *
#3. print a inverted right angled triangle pattern of * using nested loops in python programming.
for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print() #output: * * * * *, 
                #    * * * *, 
                #    * * *, 
                #    * *, 
                #    *
#so these were some basic patterns using nested loops in python programming.
#for more patterns and questions on nested loops in python programming, refer to code and debug questions statements in python programming.