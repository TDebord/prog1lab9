def encode(input):
    inputList = list(input)
    encodedList = []
    encodedString = ''
    for i in range(len(inputList)):
        if int(inputList[i]) <= 6:
            encodedList.append(int(inputList[i])+3)
        else:
            encodedList.append(int(inputList[i])-7)
        encodedString += str(encodedList[i])
    return encodedString

tester = encode('00009988')
print(tester)