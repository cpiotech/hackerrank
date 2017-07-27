class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return repr((self.name, self.score))
    def comparator(self, a, b):
        val = b.score - a.score
        if val == 0:
            if a.name < b.name:
                return -1
            else:
                return 1
        return val
