import sys
import binascii

def main():
    if len(sys.argv) != 2 :
        raise ValueError("Please provide a hex value to convert.")
    
    hexconvert = sys.argv[1]

    try:
        hexed = binascii.unhexlify(hexconvert) 
    except TypeError:
        hexed = "Not a valid hex string"


    return hexed



