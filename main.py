# Name: Oixel Romero
# Lab: Lab 6 - Version Control
# October 25th, 2023

encoded_password = ''


# Takes a password string and adds 3 to each character
def encode(password):
    # Stores string for concatenation
    new_password = ''

    # Runs through every character in string and adds 3 to it
    for i in range(len(password)):
        num = int(password[i])
        new_char = str(num + 3)

        # Concats new character to entire string
        new_password = new_password + new_char
    return new_password
def decode(password):
    decoded_password = ''
    for i in password:
        decoded_char = int(i) - 3
        if decoded_char < 3:
            decoded_char += 7
        decoded_char = str(decoded_char)
        decoded_password += decoded_char
    return decoded_password


def main():
    # Pulls global variable into function
    global encoded_password

    # Outputs basic menu
    print('Menu')
    print('----------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    # Gets user's choice from menu
    choice = input('Please enter an option: ')

    if choice == '1':  # Encode
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    elif choice == '2':  # Decode
        decoded_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
    elif choice == '3':  # Quit
        return


if __name__ == "__main__":
    main()

