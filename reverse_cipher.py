#encrypt
'''
message = input("Enter message to encrypt: ")
translated = ""
i = len(message)-1
while i >= 0:
    translated = translated + message[i]
    #print("i is",i,", message[i] is",message[i],", translated is", translated)
    i = i - 1

print(translated)

#The program turns the message around, last letter becomes first and so on

#decrpyt

message = translated
translated = ""
i = len(message)-1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

#print(len("Hello world!"))
#print(len("Hello" + " "+ "world!"))


message = input("What would you like to do?\nEncrypt\nDecrypt\n")
if message == "Encrypt":
    print("Your message will be encrypted\n")
    message = input("Enter your message: ")
    x1 = message
    translated = ""
    i = len(message)-1
    while i >= 0:
        translated = translated + message[i]
        i = i-1
    print(translated)
elif message == "Decrypt":
    print("Your message will be encrypted\n")
    message2 = input("Enter the encrypted messagte: ")
    y1 = message2
    translated = ""
    i = len(message2)-1
    while i >= 0:
        translated = translated + message2[i]
        i = i-1
    print(translated)

'''

def Encryptmessage(str, key1):
    encstring = ""
    for i in str:
        if(ord(i)) >= 65 and (ord(i) <= 90):
            tempstr = (ord(i) + key1)
            if tempstr > 90:
                tempstr = tempstr%90 + 64
            encstring = encstring + chr(tempstr)
        elif(ord(i))>97 and (ord(i)) <= 122:
                tempstr = (ord(i) + key1)
                if tempstr > 122:
                     tempstr = tempstr%122+96
                encstring = encstring + chr(tempstr)
        else:
             encstring = encstring + chr(ord(i) + key1)
    return encstring

def Decryptmessage(key1):
    ptr1 = Encryptmessage(str, key1)
    dncstring = ""
    for i in ptr1:
        if((ord(i))>=65) and (ord(i))<=90:
            dncstring = dncstring + chr((ord(i) - key1 - 65) % 26 + 65)
        elif ((ord(i)) >=97) and (ord(i)) <= 122:
             dncstring = dncstring + chr((ord(i) - key1 - 97) % 26 + 97)
        else:
             dncstring = dncstring + chr(ord(i) - key1)
    return dncstring
print("Enter the string to Encrypt and Decrypt: ")
str = input()
print("Enter the key(Eg. 11): ")
keyp = int(input())
keyp=keyp%26
print("Encrypted string: ", Encryptmessage(str, keyp))
print("Decrypted string: ", Decryptmessage(keyp))
