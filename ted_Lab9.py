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

def decode(input):
    decode_input_list = []
    string = str()
    for i in input:
        decode_input_list.append(int(i))
    for i in range(0,len(decode_input_list)-1):
        i = i-3
        if i == -1:
            i = 9
            string+=str(i)
        if i == -2:
            i = 8
            string+=str(i)
        if i == -3:
            i = 7
            string+=(str(i))
        string += str(i)
    return string
            





while(True):
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
    menuSelection = int(input("Please enter an option: "))

    if(menuSelection == 1):
        valPreEncode = str(input("Please enter your password to encode: "))
        valPostEncode = encode(valPreEncode)
    elif(menuSelection == 2):
        decode(valPostEncode)
        print("The encoded password is ", valPostEncode, ", and the original password is ", valPreEncode,".",sep='')
    else:
        break
