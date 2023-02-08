### docstrings
### docstrings are a way to create little bits of documentation in our code as we go along
### here is an example of assigning a docstring to your function using """write something""" on the first line of your function. 
def format_name(first_name, last_name):
    """Take first and last name and capitalize the first letter in each then return those strings as one full name."""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = first_name + " " + last_name
    return full_name

print(format_name("riLey", "frANcis"))