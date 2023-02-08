### functions with outputs 
### building a calculator app
import art
print(art.logo)

def calculator(number1, opperator, number2):
    final_answer = 0
    if opperator == "+":
        final_answer = number1 + number2
    elif opperator == "-":
        final_answer = number1 - number2
    elif opperator == "/":
        final_answer = number1 / number2
    elif opperator == "*":
        final_answer = number1 * number2
    return final_answer

def instructions_function():
    first_number = float(input("What is the first number?:"))

    continue_calculating = ""
    while continue_calculating != "n":
        if continue_calculating == "":
            print("+")
            print("-")
            print("/")
            print("*")
        opperation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        answer = calculator(first_number, opperation, second_number)
        print(f"{first_number} {opperation} {second_number} = {answer} ")
        first_number = answer

        continue_calculating = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")



continue_calculating = ""
while continue_calculating == "n" or continue_calculating == "":
    instructions_function()


