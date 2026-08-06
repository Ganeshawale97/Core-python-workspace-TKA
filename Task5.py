#MEMORY ADDRESS ID CARD INPUT FORM CONSOLE

name = input("enter your name: ")
age = input("enter your age: ")
city = input("enter your city: ")
phone_number = input("enter your phone number: ")
dob = input("enter your dob (DD/MM/YYYY): ")
blood_group = input("enter your blood group: ")

print("Memory Address of Name : ", id(name))
print("Memory Address of Age : ", id(age))
print("Memory Address of City : ", id(city))
print("Memory Address of Phone Number : ", id(phone_number))
print("Memory Address of Date of Birth : ", id(dob))
print("Memory Address of Blood Group : ", id(blood_group))