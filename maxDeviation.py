n = int(input("How many numbers do you want to input:"))
highNum = 0
lowNum = 101
while n:
    num = int(input("Enter the number: "))
    if num >= 0 and num <= 100:
        if highNum < num:
            highNum = num
        if lowNum > num:
            lowNum = num
    n = n - 1
deviation = highNum - lowNum

print(highNum)
print(lowNum)
print("Highest Deviation:", deviation)
