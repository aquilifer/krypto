#!/bin/python

import sys
import optparse

#My own modules
import common

        
def encrypt(msg, key):
    uMsg = common.upcaseInAllWords(msg)
    cMsg = []
    for w in uMsg:
        cWrd = []
        for l in w:
            v = ord(l) + int(key)
            if v > ord('Z'):
                v = v - ord('Z') + (ord('A') - 1) 
                if v > ord('Z') : #In case of decryption the key may be >26
                    v = v - ord('Z') + (ord('A') - 1) 
            c = chr(v)
            cWrd.append(c)
        cMsg.append(cWrd)
    return common.joinArrayIntoString(cMsg)

def decrypt(msg, key):
    return encrypt(msg, int(key) + 26)

def main():
    """
    """
    parser = optparse.OptionParser()
    parser.add_option("-d", "--decrypt",
                      action="store_true",
                      dest="decrypt",
                      default=False,
                      help="Set to decrypt a message.")
    parser.add_option("-e", "--encrypt",
                      action="store_true",
                      dest="encrypt",
                      default=False,
                      help="Set to encrypt a message.")
    parser.add_option("-k", "--key",
                      dest="key",
                      default=0,
                      help="Set mod of ceasar cipher.")
    parser.add_option("-f", "--file",
                      dest="file",
                      default=None,
                      help="")

    (options, args) = parser.parse_args()
    msg = ""
    
    if len(sys.argv) > 1:
        msg = args
    elif options.file != None:
        pass
    elif len(sys.argv) > 1 and options.file != None:
        print "Both msg and file entered."
        sys.exit(1)
    else:
        print "No msg entered."
        sys.exit(1)

    out = ""
    if options.decrypt:
        out = decrypt(msg, options.key)
        
    if options.encrypt:
        out = encrypt(msg, options.key)
        
    print out

if __name__ == "__main__":
    try:
        main()
    except:
        raise
    sys.exit(0)
