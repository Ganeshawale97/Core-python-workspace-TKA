# ==========================================
# PYTHON BASICS - DIFFERENT PRACTICE SET 2
# 25 QUESTIONS WITH CODE
# ==========================================


# 1. Employee Details
# Question: Create variables for employee name, salary, department,
# and experience and display their values.

name = "Rahul"
salary = 35000
department = "IT"
experience = 2

print("Name:", name)
print("Salary:", salary)
print("Department:", department)
print("Experience:", experience)


# 2. Convert String to Integer
# Question: Take two numbers as strings and convert them into integers.
# Display their addition.

a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print("Addition:", a + b)


# 3. Find Largest and Smallest
# Question: Find the largest and smallest number from a list.

numbers = [45, 12, 89, 34, 67]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# 4. Check Data Types
# Question: Create variables of different data types and display
# their types.

name = "Python"
age = 21
percentage = 85.5
status = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(status))


# 5. Absolute Difference
# Question: Take two numbers and find their absolute difference.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

difference = abs(a - b)

print("Absolute Difference:", difference)


# 6. Round a Number
# Question: Take a decimal number and round it to 3 decimal places.

number = float(input("Enter decimal number: "))

print("Rounded value:", round(number, 3))


# 7. Calculate Square
# Question: Take a number and calculate its square using pow().

number = int(input("Enter number: "))

print("Square:", pow(number, 2))


# 8. Basic Calculator
# Question: Take two numbers and perform addition, subtraction,
# and multiplication.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)


# 9. Compare Age
# Question: Take two ages and check which person is older.

age1 = int(input("Enter first age: "))
age2 = int(input("Enter second age: "))

print("First age is greater:", age1 > age2)
print("Second age is greater:", age2 > age1)
print("Both are equal:", age1 == age2)


# 10. Logical Operators
# Question: Check whether a student has marks greater than 50
# and attendance greater than 75.

marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

result = marks >= 50 and attendance >= 75

print("Eligible:", result)


# 11. Multiple Assignment
# Question: Assign values to three variables in one statement
# and display them.

name, age, city = "Ganesh", 20, "Pune"

print("Name:", name)
print("Age:", age)
print("City:", city)


# 12. Voting Eligibility
# Question: Take age as input and check whether the person
# is eligible to vote.

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# 13. Divisible by 5
# Question: Check whether a number is divisible by 5.

number = int(input("Enter number: "))

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# 14. Character Indexing
# Question: Using the string "Computer", display the first,
# third, and last characters.

text = "Computer"

print("First:", text[0])
print("Third:", text[2])
print("Last:", text[-1])


# 15. String Slicing
# Question: Using "Development", display the first 5 characters,
# last 4 characters, and reversed string.

text = "Development"

print("First 5:", text[:5])
print("Last 4:", text[-4:])
print("Reverse:", text[::-1])


# 16. String Formatting
# Question: Take name and age as input and display them
# using an f-string.

name = input("Enter name: ")
age = int(input("Enter age: "))

print(f"My name is {name} and I am {age} years old.")


# 17. Find Character
# Question: Check whether the letter "a" exists in a given string.

text = input("Enter a string: ")

print("a" in text)


# 18. Count Character
# Question: Count how many times the letter "o" appears
# in a given string.

text = input("Enter a string: ")

print("o count:", text.count("o"))


# 19. Check Starting Letter
# Question: Check whether a name starts with the letter "A".

name = input("Enter name: ")

print(name.startswith("A"))


# 20. Check Ending Word
# Question: Check whether a sentence ends with "Python".

text = input("Enter sentence: ")

print(text.endswith("Python"))


# 21. Split Sentence
# Question: Split a sentence into individual words.

text = "Python is easy to learn"

words = text.split()

print(words)


# 22. Join Words
# Question: Join a list of words using a space.

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# 23. Convert to Uppercase
# Question: Take a name as input and display it in uppercase,
# lowercase, and title case.

name = input("Enter name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title:", name.title())


# 24. Student Grade
# Question: Take marks and display the grade.

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# 25. Simple Restaurant Bill
# Question: Take food item, quantity, and price per item.
# Calculate and display the total amount.

food = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

print("Food Item:", food)
print("Quantity:", quantity)
print("Price:", price)
print("Total Amount:", total)