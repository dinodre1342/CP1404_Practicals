class Guitars:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        print()

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, float(self.cost))

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50
            return True
        else:
            return False

