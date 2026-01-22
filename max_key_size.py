MAX_KEY_SIZE = 26

def getMode():
    while True:
        print("Do you wish to encrypt, decrypt or brute force a message?")
        modestr = input().lower()
        if modestr in "encrypt e decrypt d brute b".split():
            return modestr[0]
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd' or 'brute' or 'b'.")

def getMessagestr():
    print("Enter your message: ")
    return input()

def getKeystr():
    keystr = 0
    while True:
        print("Enter the key number (1-%s)" % (MAX_KEY_SIZE))
        keystr = int(input())
        if (keystr >= 1 and keystr <= MAX_KEY_SIZE):
            return keystr

def getTranslatedMessagestr(modestr, messagestr, keystr):
    if modestr[0] == "d":
        keystr =- keystr
    translatedstr = ""

    for sym in messagestr:
        if sym.isalpha():
            num1 = ord(sym)
            num1 += keystr

            if sym.isupper():
                if num1 > ord("Z"):
                    num1 -= 26
                elif num1 < ord("A"):
                    num1 += 26
            elif sym.islower():
                if num1 > ord("z"):
                    num1 -= 26
                elif num1 < ord("a"):
                    num1 += 26
            
            translatedstr += chr(num1)
        else:
            translatedstr += sym
    return translatedstr

modestr = getMode()
messagestr = getMessagestr()
if modestr[0] != "b":
    keystr = getKeystr()

print("Your translated text is: ")
if modestr[0] != "b":
    print(getTranslatedMessagestr(modestr, messagestr, keystr))
else:
    for keystr in range(1, MAX_KEY_SIZE+1):
        print(keystr, getTranslatedMessagestr("decrypt", messagestr, keystr))
