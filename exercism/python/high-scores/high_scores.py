class HighScores:
    def __init__(self, scores):
        self._scores = scores
    
    @property
    def scores(self):
        return self._scores

    def latest(self):
        return self._scores[-1]
        
    def personal_best(self):
        return max(self._scores)

    def personal_top_three(self):
        three_max = []
        three_person = self._scores.copy()
        for i in range(3):
            if len(three_person) > 0:
                three_max.append(max(three_person))
                three_person.remove(max(three_person))
        return three_max
