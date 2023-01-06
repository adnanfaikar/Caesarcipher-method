# caesar cipher method

input_text = input("Input The Text : ")
# input_text = input_text.lower
# print(input_text)
key = 5
print("1. Encrypt")
print("2. Decrypt")
mode = input(">> ")

ledger = 'abcdefghijklmnopqrstuvwxyz 1234567890'
outputText = ''



for char in input_text :
    inputindex = ledger.find(char)

    # print(inputindex)
    if mode == '1' : #encrypt
        outputIndex = inputindex + key

    elif mode == '2': #decrypt
        outputIndex = inputindex - key
    
    if outputIndex >= len(ledger):
        outputIndex = outputIndex - len(ledger)
    elif outputIndex < 0:
        outputIndex = outputIndex + len(ledger)
    
    outputText = outputText + ledger[outputIndex]

print(outputText)

