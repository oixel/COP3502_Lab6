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


def main():
    global encoded_password

    print('Menu')
    print('----------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    choice = input('Please enter an option: ')

    if choice == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    elif choice == '2':
        print('WORK IN PROGRESS!')
    elif choice == '3':
        return


if __name__ == "__main__":
    main()

