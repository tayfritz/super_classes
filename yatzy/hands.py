from diceroller import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class.")
        super().__init__()

        for x in range(size):
            self.append(die_class())
        self.sort()
    
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice

class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)
    
    @property
    def one(self):
        return self._by_value(1)

    @property
    def two(self):
        return self._by_value(2)

    @property
    def three(self):
        return self._by_value(3)
    
    @property
    def four(self):
        return self._by_value(4)

    @property
    def five(self):
        return self._by_value(5)
    
    @property
    def six(self):
        return self._by_value(6)
    
    @property
    def _sets(self):
        return {
            1: len(self.one),
            2: len(self.two),
            3: len(self.three),
            4: len(self.four),
            5: len(self.five),
            6: len(self.six),
        }