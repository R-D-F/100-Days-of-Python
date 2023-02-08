#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# list_letters = (random.choices(letters, k = nr_letters))
# str_letters = ''.join(list_letters)
# list_symbols = (random.choices(symbols, k = nr_symbols))
# str_symbols = ''.join(list_symbols)
# list_numbers = (random.choices(numbers, k = nr_numbers))
# str_numbers = ''.join(list_numbers)

# print(str_letters + str_symbols + str_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

### my solution. Not sure if i am happy with it as I used shuffle and choices which are not
### things we coverd in this section

# list_letters = (random.choices(letters, k = nr_letters))

# list_symbols = (random.choices(symbols, k = nr_symbols))

# list_numbers = (random.choices(numbers, k = nr_numbers))
# print(list_numbers)

# list_all = list_letters + list_numbers + list_symbols
# print(list_all)
# random.shuffle(list_all)
# print(list_all)
# list_all_str = ''.join(list_all)
# print(list_all_str)


### This is a different solution I came up with using while loops which we also haven't 
### coverd. Below you will see the professor solution that used the for loops I should have
### idk why this didn't occur to me, I couldn't remember how to use the range function I guess.

# list_symbols = []
# list_letters = []
# list_numbers = []

# while len(list_letters) < nr_letters:
#     if len(list_letters) < nr_letters:
#         list_letters += letters[random.randint(0, 51)]

# while len(list_numbers) < nr_numbers:
#     if len(list_numbers) < nr_numbers:
#         list_numbers += numbers[random.randint(0, 9)]

# while len(list_symbols) < nr_symbols:
#     if len(list_symbols) < nr_symbols:
#         list_symbols += symbols[random.randint(0, 8)]

# full_list = list_numbers + list_letters + list_symbols
# random.shuffle(full_list)
# full_list_str = ''.join(full_list)
# print(full_list_str)

### Professor solution
### Eazy
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# print(password)

### Professor solution
### Hard
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

### Okay, I didn't do as bad as I thought. I just implemented stuff in a slightly different way. 

### hard solution not using shuffle to prove a point to myself
### doesn't work yet
# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# random_order = []
# len_password_list = len(password_list)
# for char in range(1, len_password_list + 1):
#     random_number = random.randint(0,len_password_list+1)
#     if random_number in random_order:
#         random_number = random.randint(0,len_password_list+1)
#     else:
#         random_order.append(random_number)

# print(random_order)


# password = ""
# for char in password_list:
#     password += char

# print(password)