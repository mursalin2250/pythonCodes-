n = int(input("How many numbers do you want to enter: "))
number_list = []
i = 0
while i < n:
    number = int(input("Enter the number: "))
    number_list.append(number)
    i += 1
summation = sum(number_list)
average = summation/n
print("The average is", round(average, 3))
listCopy = number_list.copy()
listCopy.sort(reverse=True)
print("The first maximum number is:", listCopy[0])
print("The second maximum number is:", listCopy[1])
