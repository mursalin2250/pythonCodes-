# vowel = ["a", "e", "i", "o", "u"]
# vowelCount = [0,0,0,0,0]
# string = "basic programming in python"
# for i in string:
#     if i in vowel:
#         loc = vowel.index(i)
#         vowelCount[loc] += 1
# print("Text:", string)
# i = 0
# while i < len(vowelCount):
#     print(vowel[i], ":", vowelCount[i], end=" ")
i = 0
text = "basic programming in python"
cntA = cntE = cntI = cntO = cntU = 0
while i < len(text):
    if text[i] == "a":
        cntA += 1
    elif text[i] == "e":
        cntE += 1
    elif text[i] == "i":
        cntI += 1
    elif text[i] == "o":
        cntO += 1
    elif text[i] == "u":
        cntU += 1
    i += 1
print("Text:", text)
print("Vowel counting:", "a:", cntA, "e:", cntE, "o:", cntO, "i:", cntI, 
      "u:", cntU,)
