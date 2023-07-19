def encode(password):
    encoded = ''
    for char in password:
        encoded += str(int(char) + 3)
        return encoded
        
#decoder function from ally
def decode(password):
        decoded = ''
        for char in password:
            decoded += str(int(char) - 3)
            return decoded
            
#newly formatted print menu options from ally
print('Menu\n')
print('-------------\n')
print('1. Encode\n')
print('2. Decode\n')
print('3. Quit\n')

option = int(input("Please enter an option "))

if option == 1:
    password = int(input("Please enter your password to encode: "))
    if len(password) != 8 or not password.isdigit:
        print(" ")


#seeing if this works

