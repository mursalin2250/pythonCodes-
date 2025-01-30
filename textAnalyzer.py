userText = input("Enter the text: ")
punctuation = [" ", ",", ":", ";", "/"]
i = 0
count = 0
flag = True
while i < len(userText):
    if userText[i] in punctuation:
        if flag == False:
            flag = True
            count += 1
        else:
            flag = False
    i += 1
if userText[0] in punctuation:
    print("Number of word:", count - 1)
elif userText[len(userText) - 1] in punctuation or userText[0] in punctuation :
    print("Number of word:", count)
else:
    print("Number of word:", count + 1)
