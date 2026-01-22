import pyperclip

msgstring = "This is Ceasar Cipher Program and this is our message."
keycode = 13
modetype = "encrypt" # set it to encrypt or decrypt
SYMBOLSTYPE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'" # all caps signals general variable
translatedstr = ""
for sym in msgstring:
    if sym in SYMBOLSTYPE:
        symindex = SYMBOLSTYPE.find(sym)
        if modetype == "encrypt":
            translatedidx = symindex + keycode
        elif modetype == "decrypt":
            translatedidx = symindex - keycode
        
        if translatedidx >= len(SYMBOLSTYPE):
            translatedidx = translatedidx - len(SYMBOLSTYPE)
        elif translatedidx < 0:
            translatedidx = translatedidx + len(SYMBOLSTYPE)
        
        translatedstr = translatedstr + SYMBOLSTYPE[translatedidx]

    else:
        translatedstr = translatedstr + sym
print(translatedstr)
pyperclip.copy(translatedstr)