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


if __name__ == "__main__":


    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        password = ""

        # Prompt for password and call encode function
        if choice == 1:
            password = input("Please enter your password to encode: ")
            password = encoder(password)
            print("Your password has been encoded and stored!")
        # quit the program
        elif choice == 3:
            break