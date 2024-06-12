# Simple Function
def add_numbers(a,b):
    """Functions to add two numbers"""
    return a+b
# Calling the function
print(add_numbers(3,4))

# Square Function
def square(a):
    print(a**2)
square(5)

# Function with default Arguments
def greet(name,message="Hello"):
    """Function to greet a person with a default message"""
    return f"{message}, {name}!"
# Calling the function
print(greet("Bob"))
print(greet("Alice", "Hi"))

# Function with Variable-Length Arguments
def sum_all(*args):
    """Function to sum all given arguments"""
    return sum(args)
# Calling the function
print(sum_all(1,2,3,4,5))

# Function with Keyword Arguments
def display_info(**kwargs):
    """Function to apply another function to given arguments"""
    for key,value in kwargs.items():
        print(f"{key}: {value}")
# Calling the function
display_info(name="John",age=30,city="New York")

# Higher-order Function
def apply_function(func,x,y):
    """Function to apply another function to given arguments"""
    return func(x,y)
def multiply(a,b):
    return a*b
# Calling the higher-order function
print(apply_function(multiply,6,7))


# Lambda Expressions
# Simple Lambda Function
square=lambda x: x*x
# Calling the lambda function
print(square(5))

# Lambda Function in map
numbers=[1,2,3,4,5,6]
squares=list(map(lambda x: x * x, numbers))
# displaying the result
print(squares)

# Lambda Function in filter
numbers=[1,2,3,4,5,6]
even_numbers=list(filter(lambda x: x%2==0, numbers))
# Displaying the result
print(even_numbers)

# Lamba function in sorted
students=[("Alice", 25),("Bob", 20),("Charlie", 23)]
sorted_students=sorted(students,key=lambda student: student[1])
# Displaying the result
print(sorted_students)


# Error Handling
# Basic Try:Except block
try:
    # code that may raise an exception
    result=10/0
except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero!")
    
# Try-Except-Else Block
try:
    # Code that may raise an exception
    result=10/2
except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero!")
else:
    # code to run if no exception occurs
    print("Division Successful!")
    
# Try-Except-Finally Block
try:
    # code that may raise an exception
    result=10/2
except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero!")
finally:
    # code to run regardless of whether an exception occurs
    print("Execution completed!")
    
# Handling Multiple Exceptions
try:
    # code that may raise an exception
    number=int(input("Enter a number: "))
    result=10/number
except ValueError:
    # code to handle the exception
    print("Invalid input! please enter a number.")
except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero!")
    
# Raising Exceptions
def check_positive(number):
    if number<=0:
        raise ValueError("Number must be positive")
try:
    check_positive(-5)
except ValueError as e:
    print(e)