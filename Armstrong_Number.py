# Armstrong Number
#
# Theory:
# An Armstrong number is a number in which the sum of each digit
# raised to the power of the total number of digits is equal to
# the original number.
#
# Example:
# 153 has 3 digits.
#
# 1³ + 5³ + 3³
# = 1 + 125 + 27
# = 153
#
# Therefore, 153 is an Armstrong number.
#
# Logic:
# 1. Store the original number.
# 2. Count the number of digits.
# 3. Extract each digit using the modulus (%) operator.
# 4. Raise each digit to the power of the number of digits.
# 5. Add all the calculated values.
# 6. Compare the sum with the original number.
# 7. If both are equal, the number is an Armstrong number.

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")