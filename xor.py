import sys, os

def xor(enc, key):
    cpt = 0
    res = ""
    for integer in enc:
        res= res + chr(ord(integer)^ord(key[cpt%len(key)]))
        cpt = cpt + 1
    return res

    
if __name__ == '__main__':        
    # let's use a fixed password for testing
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print "\nUsage: xor.py <filename> \n"
        sys.exit()
    else:
        filename = sys.argv[1]
        f = open(filename, "rb")  # binary required
        data = f.read()
        f.close()

        KEY="\x6a"
        print xor(data, KEY)

