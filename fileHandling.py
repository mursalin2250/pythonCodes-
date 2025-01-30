with open("example.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("This is a file handling example in python.")
print("File written successfully.")
with open("example.txt", "a") as file:
    file.write("!")
with open("example.txt", "r") as file:
    content = file.read()
print(content)
