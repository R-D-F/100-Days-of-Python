### Check for multiple conditions on the saem line of code and, or, not
### look at age between 45 and 55

bill = 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        if age >=45 and age <=55:
            bill = 0
        print(f"Your price is ${bill}")
    elif age >= 12:
        bill = 7
        print(f"Your price is ${bill}")
    else: 
        bill = 5
        print(f"Your price is ${bill}")
    photo = print (input("Do you want a photo y/n?"))
    if photo == "y" or "Y" or "Yes" or "yes":
        bill += 3
        print (f"Your final bill is ${bill}")
    else: 
        print(f"Your bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
