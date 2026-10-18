#so, if else is used to make decisions in programming.
#for example, if we want to check if a number is positive or negative, we can use if else statements to make that decision.
#let's say we have a variable x, and we want to check if it is positive or negative.
x = 5
if x > 0:
    print("x is a positive number")
else:
    print("x is a negative number") 
#this is a simple example of if else statement. we can also use elif statement to check multiple conditions.
#for ladder if else, we can use multiple elif statements to check multiple conditions.
x = 0
if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is a negative number")
#we can use elif statement in a ladder as much times as we want to check multiple conditions.
#now come to nested if else, we can use if else statements inside another if else statement to check multiple conditions.
x = 5
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
elif x == 0:
    print("x is zero")
else:
    if x % 2 == 0:
        print("x is a negative even number")
    else:
        print("x is a negative odd number")
#so, this is how we can use if else statements in python to make decisions in our code.