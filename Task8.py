# String Slicing - Advanced Examples

name = "Ganesh"

# Index positions:
# Positive:  G  a  n  e  s  h
#            0  1  2  3  4  5
#
# Negative: -6 -5 -4 -3 -2 -1


# 1. Positive index + Negative index
print(name[2:-2])

# Start from index 2 -> 'n'
# Stop before index -2 -> 'l'
# Output: nesh Aw


# 2. Negative index
print(name[-5:])

# Start from index -5 -> 'A'
# No stop value means go until the end
# Output: Awale


# 3. Positive + Negative + Step
print(name[1:-1:2])

# Start from index 1 -> 'a'
# Stop before index -1 -> last 'e'
# Step = 2 means skip one character each time
# Output: aehae


# 4. Negative + Negative + Negative step
print(name[-2:-10:-1])

# Start from index -2 -> 'l'
# Stop before index -10 -> 'n'
# Step = -1 means move backwards
# Output: lawA hse


# 5. Complete string reverse
print(name[::-1])

# Start is empty -> start from the end because step is -1
# Stop is empty -> continue until the beginning
# Step = -1 -> move backwards
# Output: elawA hsen aG


# 6. Every second character
print(name[::2])

# Start from beginning
# Go until the end
# Step = 2 -> take every second character
# Output: GnhAael


# 7. Reverse every second character
print(name[::-2])

# Start from the end
# Move backwards
# Step = -2 -> take every second character in reverse
# Output: eaA hnG


# 8. Reverse the first part
print(name[5::-1])

# Start from index 5 -> 'h'
# Move backwards because step = -1
# Continue until the beginning
# Output: hsen aG


# 9. Last 6 characters in reverse
print(name[-1:-7:-1])

# Start from -1 -> 'e'
# Move backwards
# Stop before -7
# Output: elawA 


# 10. Positive start + positive stop + reverse
print(name[8:2:-1])

# Start from index 8 -> 'w'
# Move backwards
# Stop before index 2 -> 'n'
# Output: wA hse