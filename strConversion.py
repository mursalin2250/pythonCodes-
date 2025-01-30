string = input("Give your input: ")
i = 0
coded_str = ""
while i < len(string):
    if (ord(string[i]) >= 97 and ord(string[i]) <= 122) or (ord(string[i]) >= 65 and ord(string[i]) <= 90):
        if string[i] == "o" or string[i] == "O":
            coded_str += "0"
        else:
            coded_str += string[i]
    i += 1
print(coded_str)
