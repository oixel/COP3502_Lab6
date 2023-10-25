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
        num = int(password[i]) + 3
        if num > 9:
            char = str(num - 10)
        else:
            char = str(num)

        # Concats new character to entire string
        new_password = new_password + char
    return new_password


def decode(password):
    decoded_password = ''
    #iterate through characters in password and add three (account for if the number turns negative when subtracting three)
    for i in password:
        decoded_char = int(i) - 3
        if decoded_char < 0:
            decoded_char += 10
        decoded_char = str(decoded_char)
        decoded_password += decoded_char
    return decoded_password


def main():
    while True:
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
            break


if __name__ == "__main__":
    main()
