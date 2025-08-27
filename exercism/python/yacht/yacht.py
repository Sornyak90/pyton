# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "thress"
FOURS = "fours"
FIVES = "five"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    points=0
    if YACHT == category:
        if all(x == dice[0] for x in dice):
            points = 50
    if ONES == category:
        points = dice.count(1)
    if TWOS == category:
        points = dice.count(2)*2
    if THREES == category:
        points = dice.count(3)*3
    if FOURS == category:
        points = dice.count(4)*4
    if FIVES == category:
        points = dice.count(5)*5
    if SIXES == category:
        points = dice.count(6)*6
    if FULL_HOUSE == category:
        digit = list(set(dice))
        if len(digit) == 2:
            if 2 <= dice.count(digit[0]) <=3 and 2 <= dice.count(digit[1]) <=3:
                points= digit[0]*dice.count(digit[0]) + digit[1]*dice.count(digit[1])
            return points
                
    if FOUR_OF_A_KIND == category:
        digit = set(dice)
        for i in digit:
            if dice.count(i) >= 4:
                points= i*4
    if LITTLE_STRAIGHT == category:
        count = 0
        for i in range(1,6):
            if i in dice:
                count+=1
        if count == 5:
            points = 30
    if BIG_STRAIGHT == category:
        count = 0
        for i in range(2,7):
            if i in dice:
                count+=1
        if count == 5:
            points = 30

    if CHOICE == category:
        points =sum(dice)

    return points
