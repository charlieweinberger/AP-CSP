import enchant
d = enchant.Dict("en_US")

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
    
        strings = []
        for i in range(26):

            text = decrypt_text(text, i)
            word_is_real = True

            for word in text.split(" "):
                if not d.check(word):
                    word_is_real = False
                    break

            if word_is_real:
                strings.append(text)
        
        return strings

print(decrypt_caesar_cipher("Kvu'a qbknl h ivvr if paz jvcly", 7))
print(decrypt_caesar_cipher("KRPCFIJNZWK"))
print(decrypt_caesar_cipher("DOOV ZHOO WKDW HQGV ZHOO"))