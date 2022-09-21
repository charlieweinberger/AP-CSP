num_friends = input("How many friends do you have? ")
num_hours = input("How many hours a day do you play video games? ")

if int(num_friends) > 0:
    has_friends = True
else:
    has_friends = False

if int(num_hours) > 2:
    gamer = True
else:
    gamer = False

if has_friends and gamer:
    print("You should play Valorant")
elif not has_friends and gamer:
    print("Go touch some grass")
elif has_friends and not gamer:
    print("You should play Among Us")
else:
    print("You should play Stumble Guys")