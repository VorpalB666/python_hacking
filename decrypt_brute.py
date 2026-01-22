messagestr = "guv6Jv6Jfrp5r7JZr66ntr"
SYMBOLSSTR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
for keystr in range(len(SYMBOLSSTR)):
    translatedstr = ""
    for sym in messagestr:
        if sym in SYMBOLSSTR:
            symindex = SYMBOLSSTR.find(sym)
            translatedidx = symindex - keystr

            if translatedidx < 0:
                translatedidx = translatedidx + len(SYMBOLSSTR)

            translatedstr = translatedstr + SYMBOLSSTR[translatedidx]
        else:
            translatedstr = translatedstr + sym
    print('Key value #%s: %s' % (keystr, translatedstr))