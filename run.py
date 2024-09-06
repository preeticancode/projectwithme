# Function to find the zodiac sign based on birthdate
def zodiac_game():
    clear()  # Clear the terminal at the start of the game
    print(Fore.CYAN + "Please enter your birthdate to find out your zodiac sign." + Style.RESET_ALL)
    
    while True:  # Loop until valid date format is entered
        # Get user's birthdate
        birthdate_str = input(Fore.YELLOW + "Enter your birthdate (YYYY-MM-DD): " + Style.RESET_ALL)
        
        # Convert the input to a date object
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            break  # Exit the loop when valid date is entered
        except ValueError:
            print(Fore.RED + "Invalid date format. Please enter the date in YYYY-MM-DD format." + Style.RESET_ALL)
            
            # Retry loop for valid input (yes or no)
            while True:
                retry = input(Fore.YELLOW + "Would you like to retry? (yes/no): " + Style.RESET_ALL).strip().lower()
                if retry == 'yes':
                    break  # Continue with the loop to retry the date input
                elif retry == 'no':
                    print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
                    sys.exit()  # Exit the game
                else:
                    print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'." + Style.RESET_ALL)

    # Get day and month from the birthdate
    day = birthdate.day
    month = birthdate.month
    
    # Determine the zodiac sign
    sign, description = get_zodiac_sign(day, month)
    
    if sign:
        print(Fore.GREEN + f"\nYour zodiac sign is {sign}!" + Style.RESET_ALL)
        print(Fore.CYAN + f"Description: {description}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Sorry, we couldn't determine your zodiac sign. Please try again." + Style.RESET_ALL)
    
    # Ask if the user wants to play again or exit with validation
    while True:
        play_again = input(Fore.YELLOW + "\nWould you like to play again or exit? (play/exit): " + Style.RESET_ALL).strip().lower()
        if play_again == 'play':
            main_menu()
            break
        elif play_again == 'exit':
            print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 'play' or 'exit'." + Style.RESET_ALL)
