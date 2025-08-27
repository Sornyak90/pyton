import random

class Robot:
    def __init__(self):
        self._name = None  

    @property
    def name(self):
        if self._name is None:
            letters = ''.join(chr(random.randint(ord('A'), ord('Z'))) for _ in range(2))
            digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
            self._name = letters + digits
        return self._name

    def reset(self):
        self._name = None
        random.seed()
        