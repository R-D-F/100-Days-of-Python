import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_y_or_n = "yes"

def ceasar(start_text, shift_amount, cypher_direction):
    if cypher_direction.lower() != "encode" and cypher_direction.lower() != "decode":
        print(f'''Command "{direction}" not recognized.''')
        quit()
    shift_alphabet = []
    for num in range(len(alphabet)):
        if cypher_direction.lower() == "encode":
            shift_alphabet += alphabet[(num + shift_amount) % len(alphabet) ]
        elif cypher_direction.lower() == "decode":
            shift_alphabet += alphabet[((num - shift_amount) % len(alphabet))]
    message = "" 
    for char in start_text:
        if char not in alphabet:
            message += char
        else:
            position = alphabet.index(char)
            char = shift_alphabet[position]
            message += char      
    print(message)


while user_y_or_n == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)
    user_y_or_n = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

