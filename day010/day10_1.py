### functions with outputs 
### building a calculator app


def calculator_app_first(number1, opperator, number2):
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

continue_calculating = ""
while continue_calculating == "n" or continue_calculating == "":
    first_number = int(input("What is the first number?:"))

    continue_calculating = ""
    while continue_calculating != "n":
        if continue_calculating == "":
            print("+")
            print("-")
            print("/")
            print("*")
        opperation = input("Pick an operation: ")
        second_number = int(input("What's the next number?: "))
        answer = calculator_app_first(first_number, opperation, second_number)
        print(f"{first_number} {opperation} {second_number} = {round(answer,4)} ")
        first_number = answer

        continue_calculating = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")



