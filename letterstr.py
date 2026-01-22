messagtestr = "PYTHON HACKING DEMO"
LETTERSTR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for keycode in range(len(LETTERSTR)):
    translatedtxt = ""
    for symbolchar in messagtestr:
        if symbolchar in LETTERSTR:
            numsym = LETTERSTR.find(symbolchar)
            numsym = numsym - keycode
            if numsym < 0:
                numsym = numsym + len(LETTERSTR)
            translatedtxt = translatedtxt + LETTERSTR[numsym]
        else:
            translatedtxt = translatedtxt + symbolchar
    print("KEYCODE #%s: %s" % (keycode, translatedtxt))