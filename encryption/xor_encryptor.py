from xor_operation import *

characters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR_encryptor(word, key):
    new_word = ""
    for i in range(len(word)):
        char_binary = encode(word[i])
        key_binary = encode(key[i % len(key)])
        new_byte = xor_byte(char_binary, key_binary)
        new_char = decode(new_byte)
        new_word += new_char
    return new_word

if __name__ == '__main__':

    xor_encryptor_tests = [
        ["hello", "world"],
        ["hi ms. orret", "to dr. jekyl"],
        ["pasadena high school", "papparazzi hide poorly"],
        ["&avrvLYpjgiWtmewbSfq bl", "Beaver believers, leave"],
        ["aaaaaankao  )lx@EAC@?wyz", "Never lend a penguin your gown"],
        ["aaaaaaaaaaaaufdInK#uaaardd!?eeejMaynC", "Never gonna frown, and roam away, adieu"]
    ]

    for test in xor_encryptor_tests:
        word, key = test
        encrypted = XOR_encryptor(word, key)
        decrypted = XOR_encryptor(encrypted, key)
        assert word == decrypted
    
    print("Passed all tests")