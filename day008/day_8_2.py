### functions with more than one input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Riley", "Bellingham")

### this is called a positional arguement because the first arg is tied to name the second is tied to the location

### keyword arguments
def my_function(a, b, c):
    print(a)
    print(b)
    print(c)
my_function(c="butts", b="guts", a="mutts")