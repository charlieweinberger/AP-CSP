from xor_operation import *

bases = ['C', 'T', 'A', 'G']

def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += xor(msg[i], key[i])
    return new_msg

def encode_DNA(character):
    char_index = bases.index(character)
    return '{0:02b}'.format(char_index)

def decode_DNA(binary):
    char_index = int(binary, 2)
    return bases[char_index]

"""

C = 00
T = 01
A = 10
G = 11 

A XOR C = 10
C XOR G = 00
G XOR T = 11
T XOR A = 01

"""

def XOR_DNA(plain_DNA, key_DNA):

    DNA_binary_map = { "C": "00", "T": "01", "A": "10", "G": "11" }
    DNA_binary = "".join([DNA_binary_map[base] for base in plain_DNA])
    key_binary = "".join([DNA_binary_map[base] for base in key_DNA])

    print(f'{DNA_binary = }')
    print(f'{key_binary = }')

    new_DNA_binary = xor_byte(DNA_binary, key_binary)
    new_DNA = decode_DNA(new_DNA_binary)

    return new_DNA

def XOR_DNA_2(plain_DNA, key_DNA):

    new_DNA = ""

    for i in range(len(plain_DNA)):

        DNA_binary = encode_DNA(plain_DNA[i])
        key_binary = encode_DNA(key_DNA[i])

        print(f'{DNA_binary = }')
        print(f'{key_binary = }')

        new_byte = xor_byte(DNA_binary, key_binary)
        new_DNA += decode_DNA(new_byte)

    return new_DNA

if __name__ == '__main__':

    word, key = "ACGT", "CGTA"
    
    encrypted = XOR_DNA(word, key)
    print(encrypted)

    encrypted_2 = XOR_DNA_2(word, key)
    print(encrypted_2)

    # assert encrypted == "AGAG"

    # decrypted = XOR_DNA(encrypted, key)
    # print(decrypted)
    # assert word == decrypted, decrypted

    print("Passed all tests")