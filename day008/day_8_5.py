alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    shift_alphabet = []
    for num in range(len(alphabet)):
        shift_alphabet += alphabet[(num + shift_amount) % len(alphabet) ]
    encrypted_message = "" 
    for char in plain_text:
        position = alphabet.index(char)
        char = shift_alphabet[position]
        encrypted_message += char
    print(encrypted_message)

def decrypt(encrypted_text, shift_amount):
    shift_alphabet = []
    for num in range(len(alphabet)):
        shift_alphabet += alphabet[((num - shift_amount) % len(alphabet))]
    decrypted_message = ""
    for char in encrypted_text:
        position = alphabet.index(char)
        char = shift_alphabet[position]
        decrypted_message += char
    print (decrypted_message)

if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text, shift)
else:
    print(f'''Command "{direction}" not recognized.''')
    