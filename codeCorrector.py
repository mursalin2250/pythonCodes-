n = int(input("Enter a positive number: "))
if n < 0:
    print("Invalid input!")
else:
    for i in range(1, n+1):
        print("The square of", i, "is", i**2)
    print("Program Complete")

