#now, we are going to learn a fundamental topic in python programming, which is functions.
#functions are a block of code that can be reused multiple times in a program.
#so, basically, functions are used to perform a specific task and can be called multiple times in a program.
#functions are defined using the def keyword, followed by the function name and parentheses.
#in easy words, functions are a way to organize our code and make it more readable and reusable.
#ex..
def greet():
    print("Hello, welcome to the world of python programming!")
#now def is used to define a function, and greet is the name of the function.
#now, we can call the function using its name followed by parentheses.
greet() #output: Hello, welcome to the world of python programming!
#i hope you have understood the concept of functions in python programming.
#functions can also take parameters, which are values that can be passed to the function when it is called.
#ex..
def greet(name):
    print("Hello, " + name + "! Welcome to the world of python programming!")
#now, we can call the function and pass a value to it.
greet("John") #output: Hello, John! Welcome to the world of python programming!
#i hope you have understood the concept of parameters in functions.
#similarly, functions can also return values, which are values that can be returned from the function when it is called.
#ex..
def add(x, y):
    return x + y
#now, we can call the function and pass values to it, and it will return the sum of those values.
result = add(5, 3)
print(result) #output: 8    
#note return statement is used to return a value from the function not to print it. we can use the returned value in our code as we want.   
# functions can also have default parameters, which are values that are used if no value is passed to the function when it is called.
#ex..
def greet(name="Guest"):
    print("Hello, " + name + "! Welcome to the world of python programming!")
#now, we can call the function without passing a value, and it will use the default value.
greet() #output: Hello, Guest! Welcome to the world of python programming!
#note, if else and loops can also be used inside functions to make decisions and repeat tasks in our code.
#that's all for now, i hope you have understood the concept of functions in python programming.
