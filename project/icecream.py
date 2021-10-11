"""Ice cream module

Contains classes all about ice cream, well known to be nature's perfect food.
"""

# This new file is a "module" -- a file containing
# Python code that others can also use.  (Known in other
# languages as a "library")

# I've defined a new class a-- a new type of data --
# that I can then create new "instances" of

class Scoop:
    """Models one scoop of ice cream, with a flavor."""
    def __init__(self, flavor):   # here, we set the attributes of the scoop
        self.flavor = flavor

class Bowl:
    """Models a bowl of ice cream, in which the scoops are
    stored in a list, known as "self.scoops"
    """
    def __init__(self):
        self.scoops = []

    def add_scoop(self, one_scoop):
        self.scoops.append(one_scoop)

# only execute this stuff if we're running icecream.py
# as a program.  Ignore below this line if we import it
# as a module.
if __name__ == '__main__':

    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')

    print(s1.flavor)
    print(s2.flavor)

    b = Bowl()
    b.add_scoop(s1)
    b.add_scoop(s2)