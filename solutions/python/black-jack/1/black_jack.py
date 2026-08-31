"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
        
    return int(card)

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Return the correct value of the ace (1 or 11)."""
    if card_one == 'A' or card_two == 'A':
        return 1
    current_hand = value_of_card(card_one) + value_of_card(card_two)
    if current_hand + 11 <= 21:
        return 11
        
    return 1

def is_blackjack(card_one, card_two):
    ten_cards = ('10', 'J', 'Q', 'K')
    
    return (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards)

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)
def can_double_down(card_one, card_two):
    if value_of_card(card_one)+value_of_card(card_two) in (9,10,11):
        return True
    return False