def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(byte, key):
    new_byte = ""
    for i in range(len(byte)):
        new_byte += xor(byte[i], key[i])
    return new_byte

if __name__ == '__main__':
    assert xor_byte("1100", "0101") == "1001"
    print("Passed all tests")