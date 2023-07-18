def encode(password):
    encoded = ''
    for char in password:
        encoded += str(int(char) + 3)
        return encoded

def decode(password):
        decoded = ''
        for char in password:
            decoded += str(int(char) - 3)
            return decoded



print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")
option = int(input("Please enter an option "))

if option == 1:
    password = int(input("Please enter your password to encode: "))
    if len(password) != 8 or not password.isdigit:
        print(" ")




