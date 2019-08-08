import sys
import os
import string

ALPHABET = string.ascii_uppercase
base_offset = ord(ALPHABET[0])

def main(key, plaintext):
    ciphertext=""
    key = key.upper()
    plaintext = plaintext.upper().strip(" ")
    index = 0 
    key_index = 0
    while index < len(plaintext):
        if (ord(plaintext[index])>128 or ord(plaintext[index])<base_offset):
            print("[WARNING] found non ascii caracter, skipping: " + plaintext[index])
            ciphertext += plaintext[index]
            index += 1
            continue
        k = ord(key[key_index % len(key)])

        c = chr(((ord(plaintext[index]) + k ) % 26)+base_offset)

        ciphertext+=c
        index += 1
        key_index += 1

    return ciphertext



if __name__=="__main__":
    if (len(sys.argv)<3 or len(sys.argv)>4):
        print("[ERROR] Wrong number of arguments, try python3 " + os.path.basename(__file__) + " <KEY> <PLAINTEXT>")
        sys.exit(0)
    print(main(sys.argv[1],sys.argv[2]))
