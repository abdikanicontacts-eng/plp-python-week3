# bug_hunt.py

count = 1
total = 0

# BUG: Changed the loop condition from `count < 5` to `count <= 5` so that the number 5 is included in the summation (silent logic bug).
# BUG: Added the missing colon (:) at the end of the while statement to resolve a SyntaxError.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted the integer variable `total` to a string using str() to fix the TypeError caused by directly concatenating a string and an integer.
print("Sum of 1 to 5 is: " + str(total))