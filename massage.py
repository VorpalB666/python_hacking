messagetext = input("\nEnter your text: ")
shiftcode = int(input("How many places to shift? "))
lowerAlphastr = 'abcdefghijklmopqrstuvwxyz'
upperAlphastr = lowerAlphastr.upper()
numberscode = "0123456789"
beforestr = lowerAlphastr + upperAlphastr + numberscode
afterstr = lowerAlphastr[shiftcode:] + lowerAlphastr[:shiftcode] + \
    upperAlphastr[shiftcode:] + upperAlphastr[:shiftcode] +\
          numberscode[shiftcode:] + numberscode[:shiftcode]
translationstr = str.maketrans(beforestr, afterstr)
cipherTextstr = messagetext.translate(translationstr)
print("\n Coded Message is: {}".format(cipherTextstr))
print("\nFrom: {}".format(beforestr))
print("  To: {}\n".format(afterstr))




#https://www.coursera.org/learn/python-hacking-apply-implement-analyze/lecture/lCEFw/python-hacking-demo