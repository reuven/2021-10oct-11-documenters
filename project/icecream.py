# This new file is a "module" -- a file containing
# Python code that others can also use.  (Known in other
# languages as a "library")

# I've defined a new class a-- a new type of data --
# that I can then create new "instances" of

class Scoop:
    def __init__(self, flavor):   # here, we set the attributes of the scoop
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')

print(s1.flavor)
print(s2.flavor)
