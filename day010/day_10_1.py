# ### functions with outputs
# def my_function():
#     result = 3 * 2
#     return result
# ### return replaces the function when called so that if you:
# output = my_function()
# ### output = result

# ### Functions with Outputs
# def format_name(first_name, last_name):
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     full_name = first_name + " " + last_name
#     return full_name

# print(format_name("riLey", "frANcis"))

### in a function with a return statement nothing gets returned after the return statement
### this can be useful and is called an "early return"
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = first_name + " " + last_name
    return full_name

print(format_name("riLey", "frANcis"))