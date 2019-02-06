class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores)
    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]
    def report(self):
        latest = self.scores[-1] 
        l_str = f"Your latest score was {latest}. "
        diff = max(self.scores) - latest
        if diff <= 0: return l_str + "That's your personal best!"
        return l_str + f"That's {diff} short of your personal best!"
