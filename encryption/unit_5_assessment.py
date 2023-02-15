from xor_operation import *

binary_map = { "000": "A", "001": "B", "010": "H", "011": "L", "100": "I", "101": "O", "110": "R", "111": "Y" }

def encode(character):
    bases = list(binary_map.values())
    index = bases.index(character)
    return '{0:03b}'.format(index)

def decode(binary):
    new_text = ""
    for i in range(int(len(binary) / 2)):
        new_text += binary_map[binary[i] + binary[i+1] + binary[i+2]]
    return new_text

def XOR(text, key):
    new_text = ""
    for i in range(len(text)):
        text_binary = encode(text[i])
        key_binary = encode(key[i])
        new_byte = xor_byte(text_binary, key_binary)
        new_text += decode(new_byte)
    return new_text

if __name__ == '__main__':
    decrypted = XOR("YRRORB", "OHBOOH")
    print(decrypted)