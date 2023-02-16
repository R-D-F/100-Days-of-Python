#list comprehension
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# name = "Angela"

# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num * 2 for num in range(1, 5)]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fredie"]
caps_names = [name.upper() for name in names if len(name)> 5]
print(caps_names)