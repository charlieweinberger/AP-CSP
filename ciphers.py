alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt_text(text, i):

    original = ""

    for char in text:
    
        if char not in alphabet:
            original += char

        else:
            index = alphabet.index(char)
            new_index = (index - i) % 26
            original += alphabet[new_index]
    
    return original

def decrypt_caesar_cipher(text, key=None):
    
    text = text.lower()
    
    if key != None:
        return decrypt_text(text, key)
    else:
        return [decrypt_text(text, i) for i in range(26)]

print(decrypt_caesar_cipher("Kvu'a qbknl h ivvr if paz jvcly", 7))
print(decrypt_caesar_cipher("KRPCFIJNZWK"))
print(decrypt_caesar_cipher("DOOV ZHOO WKDW HQGV ZHOO"))