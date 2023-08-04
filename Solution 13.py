def nextCard(cards):
    if not cards:
        return None, []
    next_card = cards[0]
    new_hand = cards[1:] + [cards[0]]
    return next_card, new_hand

def checkConsecutivePairs(cards):
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            print("Consecutive identical pair found:", cards[i], "and", cards[i + 1])
cards = [1, 5, 3, 4, 2, 3, 2]
for _ in range(len(cards)):
    card, cards = nextCard(cards)
    print(card)

checkConsecutivePairs(cards)
