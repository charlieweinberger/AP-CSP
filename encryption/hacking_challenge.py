# Problem set 1

print("\nProblem set 1")

a = 10
b = 5
c = (a + b) / (a - b)
d = b + c - a
e = a + b + c + d

print(a, b, c, d, e) # 10, 5, 3, -2, 16

# Problem set 2

print("\nProblem set 2")

screen = "on"
ms_orret_location = "at desk"

color_list = ["red", "yellow", "green", "white"]

print("solve in this order")

if screen != "on" and ms_orret_location != "at desk":
    color_list.reverse()

for color in color_list:
    print(color) # red, yellow, green, white

# Problem set 3

print("\nProblem set 3")

panagram = { "Mr": "Ba", "Jock": "Ckrx", "TV": "DL", "Quiz": "Emsy", "PhD": "FnT", "bags": "gouz", "few": "hpv", "lynx": "iqwj" }
values = ["hswt", "dnp", "vakwu", "dsbp", "gq", "dnp", "gpii"]

ans = {}
for value in values:
    key = ""
    for char in value:
        for k, v in panagram.items():
            v_lower = v.lower()
            if char in v_lower:
                index = v_lower.index(char)
                key += k[index]
    ans[key] = value

print(ans) # {'finD': 'hswt', 'The': 'dnp', 'wrong': 'vakwu', 'TiMe': 'dsbp', 'by': 'gq', 'bell': 'gpii'}
print(' '.join([item.lower() for item in ans.keys()])) # find the wrong time by bell

# green card

print("\nGreen card")

blanks = "deb", "ace", "add"
print(f"Answer: \"Ms. Orret, aka '{blanks[0]}', hopes you will '{blanks[1]}' the AP exam and remember to '{blanks[2]}' these points together.\"")
print(f"Blanks: {blanks}")

# red card

print("\nRed card")

alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
string = "tai ymzk iuzpaie mdq uz ftq oxmeedaay"
# https://inventwithpython.com/cipherwheel/

new_string = ""
cipher_key = 14

for char in string:
    if char != " ":
        new_string += alphabet[alphabet.index(char) + cipher_key]
    else:
        new_string += " "

print(f"Cipher key: {14}")
print(f"Answer: \"{new_string}\"")

# yellow card

print("\nYellow card")

