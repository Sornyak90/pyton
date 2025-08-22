import random, math

class Character:
    def __init__(self):
        self._strength = None
        self._dexterity = None
        self._constitution = None
        self._intelligence = None
        self._wisdom = None
        self._charisma = None

    @property
    def strength(self):
        if self._strength is None:
            self._strength = self.ability()
        return self._strength

    @property
    def dexterity(self):
        if self._dexterity is None:
            self._dexterity = self.ability()
        return self._dexterity
    @property
    def constitution(self):
        if self._constitution is None:
            self._constitution = self.ability()
        return self._constitution
    @property
    def intelligence(self):
        if self._intelligence is None:
            self._intelligence = self.ability()
        return self._intelligence
    @property
    def wisdom(self):
        if self._wisdom is None:
            self._wisdom = self.ability()
        return self._wisdom
    @property
    def  charisma(self):
        if self._charisma is None:
            self._charisma = self.ability()
        return self._charisma
    
    def ability(self):
        return random.randint(3,18)
    
    @property
    def hitpoints(self):
        return 10 + modifier(self._constitution)


def modifier(value):
    a = math.floor((value - 10)/2)
    return a




a = Character()
print(a.strength)





