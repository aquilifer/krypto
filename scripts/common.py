import sys

def divideStringIntoArray(msg):
    """supports text and array of text
    """
    out = []
    if isString(msg):
        out = msg.split()
    elif isString(msg[0]):
        for w in msg:
            out += w.split()
    else:
        out = msg            
    return out

def joinArrayIntoString(msg):
    """joins letters of two levels of lists at most. Adds a space between each list
    """
    out = ""
    if isString(msg):
        out = msg
    elif isString(msg[0]):
        for l in msg:
            out += l
    elif isString(msg[0][0]):
        for w in msg:
            for l in w:
                out += l
            out += ' '
    else:
        out = msg   #More then two layers of lists
    return out

def isString(a):
    """checks if a is of the type str
    """
    if hasattr(a, 'lower'):
        return True
    else:
        return False

def upcaseInAllWords(msg):
    """Changes all text into UPPERCASE and returns an array of words
    """
    m = divideStringIntoArray(msg)
    uMsg = []
    for word in m:
        uWord = word.upper()
        uMsg.append(uWord)
    return uMsg

###############KEYBOARD LAYOUT##################
global kb   #keyboard

#A "enum"
class Keyboard:
    en = 0
    sv = 1

def setKeyboard(keyboard):
    if keyboard == Keyboard.en:
        global kb
        pass
    elif keyboard == Keyboard.sv:
        pass
    else:
        #Board not supported
        sys.exit(1)
