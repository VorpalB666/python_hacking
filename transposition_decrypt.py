import math, pyperclip

def main():
    mymessagestr = "Paosycustkrahisgoneeng .  mhce"
    mykeystr = 8

    plaintextstr = decryptmessagestr(mykeystr, mymessagestr)

    print(plaintextstr + "|")
    pyperclip.copy(plaintextstr)

def decryptmessagestr(keystr, messagestr):
    noofcolumns = int(math.ceil(len(messagestr)/float(keystr))) #math.ceil always rounds up, opposite is math.floor, which always rounds down
    noofrows = keystr
    noofshadedboxes = (noofcolumns * noofrows) - len(messagestr)
    plaintextstr = [""] * noofcolumns
    col = 0
    row = 0

    for sym in messagestr:
        plaintextstr[col] += sym
        col += 1

        if(col == noofcolumns) or (col == noofcolumns-1 and row >= noofrows - noofshadedboxes):
            col = 0
            row += 1
    
    return "".join(plaintextstr)

if __name__ == "__main__":
    main()