
from ast import Try


alphabet=["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
"a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(start_text,shift,cipher_direction):
    end_text=""
    if cipher_direction == 'decode':
        shift *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text+=char
    print(f"Your {cipher_direction}d text is '{end_text}'")
end_the_game=False
while not end_the_game:
    direction=input("Type 'encode' for encrypt 'decode' for decrypt: ").lower()
    text=input("Enter your messege: ").lower()
    try:
        shift=int(input("Enter Shift number"))
    except:
        print("Invalid input")
        break
    shift = shift % 26
    ceaser(start_text=text,shift=shift,cipher_direction=direction)
    restart=input("Type 'yes' if you want to go again \n otherwise type 'no': ").lower()
    if restart == "no":
        end_the_game=True
