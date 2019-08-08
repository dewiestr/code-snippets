import sys
import os
import string

ALPHABET = string.ascii_uppercase
base_offset = ord(ALPHABET[0])

def main(rotation, plaintext):
    ciphertext=""
    try:
        rotation = int(rotation)
        if rotation > 25:
            print("[WARINING]: rotation larger than 25... taking modulus.")
            rotation = rotation % 26 
        pass
    except Exception as e:
        print("[ERROR]: are you sure you entered a valid integer as rotation ?")
        raise e
    
    plaintext = plaintext.upper()

    for index in range(0,len(plaintext)):
        if (ord(plaintext[index])>128 or ord(plaintext[index])<base_offset):
            print("[WARNING] found non ascii caracter, skipping: " + plaintext[index])
            ciphertext += plaintext[index]
            continue
        c = chr(((ord(plaintext[index])+rotation+base_offset)%26) + base_offset)
        ciphertext+=c
    return ciphertext



if __name__=="__main__":
    if (len(sys.argv)<3 or len(sys.argv)>4):
        print("[ERROR] Wrong number of arguments, try python3 " + os.path.basename(__file__) + " <ROTATION> <PLAINTEXT>")
        sys.exit(0)
    print(main(sys.argv[1],sys.argv[2]))
