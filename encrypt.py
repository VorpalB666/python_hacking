def encrypttext(textstr, scode):
    resultstr = ''
    for i1 in range(len(textstr)):
        charstr = textstr[i1]
        if (charstr.isupper()):
            resultstr += chr((ord(charstr) + scode - 65) % 26 + 65)
        else:
            resultstr += chr((ord(charstr) + scode - 97) % 26 + 97)
    return resultstr
textstr = "CEASAR CIPHER EXTRA EXAMPLE IN PYTHON HACKING"
scode = 5
print('Actual Text is: ' +  textstr)
print('Shift Pattern Code is: ' + str(scode))
print('Cipher Text:' + encrypttext(textstr, scode))