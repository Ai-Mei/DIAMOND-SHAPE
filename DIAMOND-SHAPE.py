import pyfiglet

def print_diamond():
    while True:
        try:
            n_input = int(input("\n\033[0m\033[1;35mInput an odd integer: \033[47m"))
            print("\033[0m\033[0;93m")
            if n_input % 2 != 0:
            # Prints the upper part of the diamond
                for i in range(1, n_input + 1, 2):
                    no_spaces = (n_input - i) // 2
                    print(" " * no_spaces, "*" * i, " " * no_spaces)
            # Prints the lower part of the diamond
                for i in range(n_input - 2, -1, -2):
                    no_spaces = (n_input - i) // 2
                    print(" " * no_spaces, "*" * i, " " * no_spaces)
                break
            else:
                # Ask the user to input an odd integer if the input is even.
                print("\033[0m\033[1;31m⚠️  Oops, it seems like it's not an odd integer. Please try again. ❌\033[0m\n")
        except ValueError:
            # Handle the error if the user input a string, instead of integer.
            print("\033[0m\033[1;31m⚠️  Error. Your input is not a number. ❌\033[0m\n")

# Banner
print("\033[0;96m𓆩⟡𓆪" * 20)
banner = pyfiglet.figlet_format("DIAMOND", font = "kban")
print("\033[0;93m", banner)
print("\033[0;96m𓆩⟡𓆪" * 20)

# Make an option if the user wants to use the program again.
while True:
    print_diamond()
    print("\n")
    print("\033[0;32m=" * 70)
    while True:
        choice = input("\n\033[1;96mDo you wish to input another odd integer? Type yes or no: \033[47m").lower()
        print("\033[0m")
        if choice == "no":
            print("\033[0;32m=" * 70)
            print("Thank you for using the diamond shape program. Goodbye!")
            print("₊˚ʚ ᗢ₊˚✧ ﾟ." * 6)
            print("\n")
            exit()
        elif choice == "yes":
            print("\033[0;32m=" * 70)
            break
        else:
            print("\033[0m\033[1;31m⚠️ Invalid input. Please type 'yes' or 'no'. ❌\033[0m\n")



