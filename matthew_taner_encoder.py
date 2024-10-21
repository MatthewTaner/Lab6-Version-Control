def print_menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


# takes a the password string and returns encoded version
def encoder(original):
    encoded = ""

    # iterate through the original string and encode
    for value in original:
        encoded += str(int(value) + 3)

    return encoded

#Function developed by Brandon Young
def decoder(encoded_password): #Password decoder that takes in 8-digit string and returns with each value shifted down 3
    decoded_password = ''
    for element in str(encoded_password):
        element = int(element) - 3
        decoded_password += str(element)
    return decoded_password

if __name__ == "__main__":

    password = ''
    encoded_password = ''
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))

        # Prompt for password and call encode function
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")

        # Decodes stored user password  using decoder function
        elif choice == 2:
            decoder(password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}\n')

        # quit the program
        elif choice == 3:
            break