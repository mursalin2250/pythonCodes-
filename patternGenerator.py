n = -1
while n < 0:
    n = int(input("Enter the number of rows: "))
    print("Invalid input!")
for i in range(1, n + 1):
    print("*" * i)
    i += 1