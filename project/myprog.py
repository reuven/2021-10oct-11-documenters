# comments are for the developers/maintainers
# API documentation is for the people who will call/use the function
#  we write API documentation in Python in "docstrings"
#  meaning: if a string (text) is the first line of a function, that the doc

def hello(name):
    """A friendly function for anyone wanting a friendly greeting

    Expects: A string, assigned to name
    Modifies: Nothing at all
    Returns: A string, with a friendly greeting

    """
    return f'Hello, {name}!'


print(hello('Reuven'))
