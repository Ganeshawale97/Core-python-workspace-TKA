marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade: A+")
    print("Result: Excellent")

elif marks >= 75:
    print("Grade: A")
    print("Result: Very Good")

elif marks >= 60:
    print("Grade: B")
    print("Result: Good")

elif marks >= 40:
    print("Grade: C")
    print("Result: Pass")

else:
    print("Grade: F")
    print("Result: Fail")
