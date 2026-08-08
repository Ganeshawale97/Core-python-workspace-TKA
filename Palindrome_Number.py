# Palindrome Number
#
# Theory:
# A palindrome number is a number that remains the same
# when its digits are reversed.
#
# Examples:
# 121 → Palindrome
# 1331 → Palindrome
# 123 → Not a Palindrome
#
# Logic:
# 1. Store the original number.
# 2. Extract the last digit using the modulus (%) operator.
# 3. Build the reversed number.
# 4. Remove the last digit using floor division (//).
# 5. Compare the original number with the reversed number.
# 6. If both are equal, the number is a palindrome.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")