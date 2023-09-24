from models.rating import Rating

class BestMatch:
    def __init__(self, ratings, bestMatch, bestMatchIndex):
        self.ratings = ratings
        self.bestMatch = bestMatch
        self.bestMatchIndex = bestMatchIndex

    def __str__(self):
        return f'{self.bestMatchIndex}:{self.bestMatch}'
