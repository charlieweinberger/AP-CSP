def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += xor(msg[i], key[i])
    return new_msg

def char_to_binary(char):
    return bin(ord(char)).replace("b", "")

def xor_word(word, key):
    new_msg = ""
    for i in range(len(word)):
        char_binary = char_to_binary(word[i])
        key_binary = char_to_binary(key[i % len(key)])
        new_byte = xor_byte(char_binary, key_binary)
        new_msg += chr(int(new_byte))
    return new_msg

# print(xor_byte("1100", "0101"))
print(xor_word("hello", "ab"))