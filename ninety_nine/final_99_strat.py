import random

computerList = ['A', 2, 5, 8, 10]

def getRandomElem():
    return random.choice(1 if card == 'A' else card for card in computerList)

def returnCard(pot, card):
    if card == 1 or card == 11: computerList.remove('A')
    else: computerList.remove(card)
    return pot + card

def computerTurn(pot):
    
    if pot >= 99:
        return returnCard(pot, getRandomElem())

    if 'A' in computerList and (pot == 87 or pot == 88):
        return returnCard(pot, 11)
        
    if 'A' in computerList and pot == 98:
        return returnCard(pot, 1)
    
    surviving_cards = []

    for card in computerList:

        if card != 'A' and pot + card <= 99:
            surviving_cards.append(card)
        
        if card == 'A' and pot <= 98:
            surviving_cards.append(1)

    if len(surviving_cards) == 0:
        return returnCard(pot, getRandomElem())
    
    return returnCard(pot, max(surviving_cards))