import random

computerList = ['A', 2, 5, 8, 10]

def computerTurn(pot):
    
    random_elem = lambda: random.choice([elem for elem in computerList if type(elem) == int])

    if pot >= 99:
        return pot + random_elem()

    if 'A' in computerList and (pot == 87 or pot == 88):
        return pot + 11
        
    if 'A' in computerList and pot == 98:
        return pot + 1
    
    surviving_cards = []

    for card in computerList:

        if card != 'A' and pot + card <= 99:
            surviving_cards.append(card)
        
        if card == 'A' and pot <= 98:
            surviving_cards.append(1)

    if len(surviving_cards) == 0:
        return pot + random_elem()
    
    return pot + max(surviving_cards)

# testing

for n in range(86, 101):
    print(f'{n}: {computerTurn(n)}')