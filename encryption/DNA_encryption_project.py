from xor_operation import *

DNA_binary_map = { "00": "C", "01": "T", "10": "A", "11": "G" }

def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += xor(msg[i], key[i])
    return new_msg

def encode_DNA(character):
    bases = list(DNA_binary_map.values())
    index = bases.index(character)
    return '{0:02b}'.format(index)

def decode_DNA(binary):
    new_DNA = ""
    for i in range(int(len(binary) / 2)):
        new_DNA += DNA_binary_map[binary[i] + binary[i+1]]
    return new_DNA

def XOR_DNA(plain_DNA, key_DNA):
    new_DNA = ""
    for i in range(len(plain_DNA)):
        DNA_binary = encode_DNA(plain_DNA[i])
        key_binary = encode_DNA(key_DNA[i])
        new_byte = xor_byte(DNA_binary, key_binary)
        new_DNA += decode_DNA(new_byte)
    return new_DNA

if __name__ == '__main__':

    word, key = "ACGT", "CGTA"

    encrypted = XOR_DNA(word, key)
    assert encrypted == "AGAG", f'{encrypted = }'

    decrypted = XOR_DNA(encrypted, key)
    assert decrypted == word, f'{decrypted = }'

    print("Passed all tests")