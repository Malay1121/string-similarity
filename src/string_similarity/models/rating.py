# Dice's Coefficient result
class Rating:
    def __init__(self, target, rating):
        self.target = target
        self.rating = rating

    def __str__(self):
        return f"'{self.target}'[{self.rating}]"
