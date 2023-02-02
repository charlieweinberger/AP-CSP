def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += xor(msg[i], key[i])
    return new_msg

if __name__ == '__main__':
    assert xor_byte("1100", "0101") == "1001"
    print("Passed all tests")