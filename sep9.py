# Task 1: Count Vowels in a String

from asyncio import Task


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

s = input("Enter a string to count vowels:- ")
total_vowels = count_vowels(s)
print(f"Total vowels in '{s}' is = {total_vowels}")


# Task 2: Check if a Number is Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime:- "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



# SCOPE IN PYTHON
# ================

# 1. Global Scope
#    - Variables defined outside any function.
#    - Accessible everywhere in the file, including inside functions (read-only by default).
#    - To modify a global variable inside a function, use the 'global' keyword.

# 2. Local Scope
#    - Variables defined inside a function.
#    - Only exist while the function is running; not accessible outside it.
#    - A local variable can have the same name as a global one — they are
#      two separate variables (local "shadows" global inside that function).

# Example:
# --------
a = 10          # global scope
print(a)        # 10

def f1():
    a = 100     # local scope (different variable than global 'a')
    print(a)    # 100

f1()
print(a)        # 10 -> unchanged, because f1()'s 'a' was local

# RETURN KEYWORD
# ==============
# - 'return' sends a value back from a function to the caller.
# - It also immediately ends the function's execution.
# - A function with no 'return' statement gives back None by default.

# Example:
# --------
def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7

# Q. what is the return keyword in python?
# RETURN KEYWORD
# ===============
# -> It is a keyword in Python.
# -> It is used to return data/value from inside the function body to outside the function.
# -> It is used to return data from local scope to global scope.
# -> When someone needs data from that function, then and only then use return.
# -> The return statement/keyword is the last statement of your function.
# -> Only one return statement is going to execute in one function.
# -> We can return multiple values using one return statement.


# Global scope variable
a = 10

def my_function():
    # Local scope
    a = 10
    b = 90
    # print(a)
    return b, a, "Atul Sir", 10+20j, True   # yes

res = my_function()
print(res)
print(type(res))   # <class 'tuple'>