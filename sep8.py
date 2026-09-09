# Q. What is function?
# -> Function is a subprogram, bunch of code or group of statements that perform a specific task.
# Function will execute only when it is called/invoked.

# There are two types of functions in Python:

# 1. Built-in functions: These are the functions which are already defined in Python.
# -> len(), input(), print(), type(), range(), sum(), min(), max(), enumerate(), int(), float(), bin(), oct(), str(), etc.

# 2. User-defined functions: These are the functions which are defined by the user.
# -> myprint, auls_sir_max

# There are two important things in functional programming:

# 1. Function definition: It is the process of creating a function.
# 2. Function call: It is the process of invoking a function.

# Q. How to define a function in Python?
# -> We use the 'def' keyword to define a function.

def function_name(input_parameters): # start of a function
    # function body
    pass

# Q. How to call a function in Python?
# -> We use the function name and pass the required input parameters to call a function.

#function_name(input_parameters) # function call

# Q. create a funciton to add two numbers and return the result.
print("Enter two numbers to add:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def add_two_numbers(num1, num2):
    result = num1 +num2
    return result

sum = add_two_numbers(num1, num2)
print("The sum of the two numbers is:", sum)

print("we are calling the function add_two_numbers")
add_two_numbers(10, 20 ) # function call
print("we are back to the main program after executuing the function add_two_numbers")
print("End of the program")