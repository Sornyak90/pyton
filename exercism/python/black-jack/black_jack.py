"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    jqk = ('J', 'Q', 'K')
    if card in jqk:
        result = 10
    elif card == 'A':
        result = 1
    else:
        result = int(card)
    return result
    

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    jqk = ('J', 'Q', 'K')
    one = 10 if card_one in jqk else (1 if card_one == 'A' else int(card_one))
    two = 10 if card_two in jqk else (1 if card_two == 'A' else int(card_two))

    if one > two:
        return card_one
    elif one < two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    jqk = ('J', 'Q', 'K')
    one = 10 if card_one in jqk else (11 if card_one == 'A' else int(card_one))
    two = 10 if card_two in jqk else (11 if card_two == 'A' else int(card_two))
    print(one)
    print(two)
    if one == 11 or two == 11:
        res = 1
    elif one + two < 11:
        res = 11
    else:
        res = 1
    
    return res



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    res=False
    jqk = ('10', 'J', 'Q', 'K')
    if card_one == 'A' and card_two == 'A':
        res = False
    elif (card_one == 'A' and card_two in jqk) or (card_one in jqk and card_two in 'A'):
        res = True
    
    return res


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    jqk = ('J', 'Q', 'K')
    one = 10 if card_one in jqk else (11 if card_one == 'A' else int(card_one))
    two = 10 if card_two in jqk else (11 if card_two == 'A' else int(card_two))
    
    return one == two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    jqk = ('J', 'Q', 'K')
    one = 10 if card_one in jqk else (1 if card_one == 'A' else int(card_one))
    two = 10 if card_two in jqk else (1 if card_two == 'A' else int(card_two))

    return 8 < one + two <= 11

print(is_blackjack('10', 'A'))
