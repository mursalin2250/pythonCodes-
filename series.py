firstTerm = int(input("Enter the first term: "))
d = int(input("Enter the difference: "))
n = int(input("Enter the number of terms: "))
lastTerm = firstTerm + (n - 1) * d
total = n/2 * (firstTerm + lastTerm)
print(total)
