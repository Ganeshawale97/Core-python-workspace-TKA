# Python List Methods - Advanced Examples
# 1. extend()
# 2. insert()
# 3. remove()
# 4. pop()
# 5. count()


# --------------------------------------------------
# 1. extend() - Adding multiple items dynamically
# --------------------------------------------------

students = ["Ganesh", "Kunal", "Surbhi"]

new_students = ["Srushti", "Supriya", "Soniya"]

students.extend(new_students)

print("All Students:", students)


# --------------------------------------------------
# 2. insert() - Insert based on a calculated position
# --------------------------------------------------

marks = [45, 67, 72, 89, 95]

position = 2
new_mark = 78

marks.insert(position, new_mark)

print("Updated Marks:", marks)


# --------------------------------------------------
# 3. remove() - Remove a specific item
# --------------------------------------------------

subjects = ["Python", "Java", "DBMS", "Python", "DSA"]

subjects.remove("Python")

print("After Removing Python:", subjects)


# --------------------------------------------------
# 4. pop() - Remove and store an element
# --------------------------------------------------

cart = ["Laptop", "Mouse", "Keyboard", "Headphones"]

removed_item = cart.pop(2)

print("Removed Item:", removed_item)
print("Updated Cart:", cart)


# --------------------------------------------------
# 5. count() - Count repeated values
# --------------------------------------------------

attendance = [
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent",
    "Present"
]

present_count = attendance.count("Present")
absent_count = attendance.count("Absent")

print("Present:", present_count)
print("Absent:", absent_count)


# --------------------------------------------------
# ADVANCED COMBINED EXAMPLE
# --------------------------------------------------

students = ["Ganesh", "Kunal", "Surbhi"]

# Add multiple students
students.extend(["Srushti", "Supriya"])

# Insert a student at index 1
students.insert(1, "Rahul")

# Remove a student
students.remove("Kunal")

# Remove the last student and store it
removed_student = students.pop()

print("Final Student List:", students)
print("Removed Student:", removed_student)

# Count how many times Ganesh appears
print("Ganesh Count:", students.count("Ganesh"))