# comments are for the developers/maintainers
# API documentation is for the people who will call/use the function
#  we write API documentation in Python in "docstrings"
#  meaning: if a string (text) is the first line of a function, that the doc

def hello(name):
    """This is the most amazing function ever written!

    So great, it gets a two-line docstring!"""
    return f'Hello, {name}!'


print(hello('Reuven'))
