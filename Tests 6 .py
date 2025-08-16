string = "here is the string"
binaryMessage = []
for char in string:
    ascii = ord(char)  # Get the ASCII value of the string
    binary8 = format(ascii, '08b')  #Get the 8 bit value of string from the ASCII value
    # Format function formats the string into 8 bits from 7 bits

    binaryMessage.append(binary8)
print(binaryMessage)

mybinary = ['01110011', '01111011', '01010001', '01010011', '01111111', '01110000']

for pos in range(0, len(binaryMessage)):
    for chars in range(0, 8):
        if binaryMessage[pos][chars] == '1':
            pass
