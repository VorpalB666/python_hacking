#In cryptography, a transposition cipher is a method of encryption which scrambles the positions of characters (transposition) without changing the characters themselves.

import pyperclip

def main():
    mymessagestr = "Python hacking course message."
    mykeystr = 8
    ciphertextstr = encryptMessagestr(mykeystr, mymessagestr)
    print(ciphertextstr + "|") #only a symbol for the end of the text
    pyperclip.copy(ciphertextstr)

def encryptMessagestr(keystr, messagestr):
    ciphertextstr = [""] * keystr
    for columnstr in range(keystr):
        currentidx = columnstr

        while currentidx < len(messagestr):
            ciphertextstr[columnstr] += messagestr[currentidx]

            currentidx += keystr

    return "".join(ciphertextstr)

if __name__ == '__main__':
    main()