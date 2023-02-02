def xor(bit1, bit2):
    return "0" if bit1 == bit2 else "1"

def xor_byte(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += xor(msg[i], key[i])
    return new_msg

def char_to_binary(char):
    return bin(ord(char)).replace("b", "")

def binary_to_char(binary):
    print('\nbinary_to_char')
    print(f'{binary = }')
    print(f'{int(binary, 2) = }')
    print(f'{chr(int(binary, 2)) = }')
    return chr(int(binary, 2))

def xor_word(word, key):
    new_msg = ""
    for i in range(len(word)):

        print(f'\n{i = }')
        
        print(f'{word[i] = }')
        char_binary = char_to_binary(word[i])
        print(f'{char_binary = }')

        print(f'{key[i % len(key)] = }')
        key_binary = char_to_binary(key[i % len(key)])
        print(f'{key_binary = }')

        new_byte = xor_byte(char_binary, key_binary)
        print(f'{new_byte = }')

        new_char = binary_to_char(new_byte)
        print(f'{new_char = }')

        new_msg += new_char
        print(f'{new_msg = }')

    return new_msg

# print(xor_byte("1100", "0101"))
print(xor_word("hello", "zzzzz"))