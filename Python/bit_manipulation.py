# Convert decimal number to binary
decNo = 4
binaryNo = bin(decNo)
print(binaryNo)

# Convert decimal number to specified bits (eg:- 32bit)
binary32 = "{:032b}".format(decNo)
print(binary32)

# Convert binary string to decimal 
decimalNo = int(binary32, 2)
print(decimalNo)

