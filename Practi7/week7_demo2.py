class Hero:
    """
    Class hero will provides some common attributes and methods.
    """
    def __init__(self, name="", health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return "I am hero [{}], my health is [{}]".format(self.name, self.health)

    def eat(self, food):
        if food == 'apple':
            self.health += 20
        elif food == 'fried chicken':
            self.health -= 50