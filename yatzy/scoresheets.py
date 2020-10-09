class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.one)

    def score_twos(self, hand):
        return sum(hand.two)

    def score_threes(self, hand):
        return sum(hand.three)

    def score_fours(self, hand):
        return sum(hand.four)

    def score_fives(self, hand):
        return sum(hand.five)

    def score_sixes(self, hand):
        return sum(hand.six)
