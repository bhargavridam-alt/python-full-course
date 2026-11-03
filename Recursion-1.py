#recursion is basically a function calling itself inside it.
#like a loop but it is not a loop.
#for example, if we want to print numbers from 1 to n, we can do it using recursion.
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)
#here the if statement is the base case, which stops the recursion when n becomes 0.
#and the print_numbers(n-1) is the recursive case, which calls the function again with n-1.
#so if we call print_numbers(5), it will print 1 2 3 4 5.
#now for the example of factorial, we can do it using recursion as well.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#here the if statement is the base case, which stops the recursion when n becomes 0.
#and the return n * factorial(n-1) is the recursive case, which calls the function again with n-1 and multiplies it with n.
#so if we call factorial(5), it will return 120.
#now for the example of fibonacci series, we can do it using recursion as well.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
#here the if statement is the base case, which stops the recursion when n becomes 0 or 1.
#and the return fibonacci(n-1) + fibonacci(n-2) is  the recursive case, which calls the function again with n-1 and n-2 and adds them.
#so if we call fibonacci(5), it will return 5.
#so, from this we can see that recursion is a powerful concept in programming, but it should be used with caution as it can lead to stack overflow if not implemented properly.
#if there is no base case or if the base case is not reached, the function will keep calling itself indefinitely and will eventually crash the program.
#to master recursion, we need to practice and understand the concept of base case and recursive case properly.
#i will recommend you to practice recursion problems on leetcode or codeforces to get a better understanding of it.
