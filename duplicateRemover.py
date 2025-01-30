n = int(input("Enter the number of hobbies you want to enter: "))
i = 0
j = 0
k = 0
hobbies = []
duplicate = []
while i < n:
    inp = input("Enter the hobbies: ")
    if inp in hobbies:
        indexNum = hobbies.index(inp)
        duplicate[indexNum] += 1
    elif inp not in hobbies:
        hobbies.append(inp)
        duplicate.append(1)
    i += 1

print("The hobbies and their repetition: ")
while k < len(hobbies):
    print(k+1, hobbies[k], "x", duplicate[k])
    k += 1
