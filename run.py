import os
import sys
import random
from datetime import datetime
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama for color support
init()


def clear():
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_zodiac_sign(day, month):
    """Return the zodiac sign and description based on birthdate."""
    zodiac_signs = [
        (3, 21, 4, 19, "Aries", "Courageous, determined, and confident."),
        (4, 20, 5, 20, "Taurus", "Reliable, patient, and devoted."),
        (5, 21, 6, 20, "Gemini", "Gentle, affectionate, and curious."),
        (6, 21, 7, 22, "Cancer", "Tenacious, highly imaginative, and loyal."),
        (7, 23, 8, 22, "Leo", "Creative, passionate, and cheerful."),
        (8, 23, 9, 22, "Virgo", "Loyal, analytical, and hardworking."),
        (9, 23, 10, 22, "Libra", "Cooperative, diplomatic, and fair-minded."),
        (10, 23, 11, 21, "Scorpio", "Resourceful, brave, and passionate."),
        (11, 22, 12, 21, "Sagittarius", "Generous, idealistic, and humorous."),
        (12, 22, 1, 19, "Capricorn", "Responsible, disciplined, and self-controlled."),
        (1, 20, 2, 18, "Aquarius", "Progressive, original, and independent."),
        (2, 19, 3, 20, "Pisces", "Compassionate, artistic, and intuitive.")
    ]

    for z in zodiac_signs:
        if (month == z[0] and day >= z[1]) or (month == z[2] and day <= z[3]):
            return z[4], z[5]

    return None, None


def zodiac_quiz():
    """Run a quiz on Zodiac signs."""
    clear()  # Clear the terminal before starting the quiz
    print(Fore.CYAN + "\nZodiac Quiz: Let's see how well you know the Zodiac signs!" +
          Style.RESET_ALL)

    questions = {
        "Which Zodiac sign is known for being adventurous?": "sagittarius",
        "Which Zodiac sign is known for being stubborn?": "taurus",
        "Which Zodiac sign is symbolized by the twins?": "gemini",
        "Which Zodiac sign is the most artistic?": "pisces",
        "Which Zodiac sign is associated with the lion?": "leo",
        "Which Zodiac sign is known for being analytical?": "virgo",
        "Which Zodiac sign is represented by the scales?": "libra",
        "Which Zodiac sign is known for being emotional and nurturing?": "cancer",
        "Which Zodiac sign is symbolized by the ram?": "aries",
        "Which Zodiac sign is known for being independent and original?": "aquarius"
    }

    # Randomly select 5 questions
    selected_questions = random.sample(list(questions.items()), 5)

    score = 0
    for question, correct_answer in selected_questions:
        while True:
            answer = input(Fore.YELLOW + question + " ").lower().strip()
            if answer:  # Check if the input is not blank
                break
            else:
                print(Fore.RED + "Answer cannot be blank. Please enter a valid answer." +
                      Style.RESET_ALL)

        if answer == correct_answer:
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer was {correct_answer.capitalize()}." +
                  Style.RESET_ALL)

    print(Fore.CYAN + f"\nYou got {score} out of {len(selected_questions)} correct!" +
          Style.RESET_ALL)


def zodiac_game():
    """Play the Zodiac Sign game."""
    clear()  # Clear the terminal at the start of the game
    print(Fore.CYAN + "Please enter your birthdate to find out your zodiac sign." +
          Style.RESET_ALL)

    while True:
        # Get user's birthdate
        birthdate_str = input(Fore.YELLOW + "Enter your birthdate (YYYY-MM-DD): " +
                              Style.RESET_ALL)

        # Convert the input to a date object
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            break
        except ValueError:
            print(Fore.RED + "Invalid date format. Please enter the date in YYYY-MM-DD format." +
                  Style.RESET_ALL)

            # Retry loop for valid input (yes or no)
            while True:
                retry = input(Fore.YELLOW + "Would you like to retry? (yes/no): " +
                              Style.RESET_ALL).strip().lower()
                if retry == 'yes':
                    break
                elif retry == 'no':
                    print(Fore.MAGENTA + "Returning to the main menu..." + Style.RESET_ALL)
                    main_menu()
                    return  # Return to the main menu
                else:
                    print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'." +
                          Style.RESET_ALL)

    # Get day and month from the birthdate
    day = birthdate.day
    month = birthdate.month

    # Determine the zodiac sign
    sign, description = get_zodiac_sign(day, month)

    if sign:
        print(Fore.GREEN + f"\nYour zodiac sign is {sign}!" + Style.RESET_ALL)
        print(Fore.CYAN + f"Description: {description}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Sorry, we couldn't determine your zodiac sign. Please try again." +
              Style.RESET_ALL)

    # Ask if the user wants to play again or return to the main menu
    while True:
        play_again = input(Fore.YELLOW + "\nWould you like to play again or return to the main menu? (play/menu): " +
                          Style.RESET_ALL).strip().lower()
        if play_again == 'play':
            zodiac_game()
            break
        elif play_again == 'menu':
            print(Fore.MAGENTA + "Returning to the main menu..." + Style.RESET_ALL)
            main_menu()
            break
        else:
            print(Fore.RED + "Invalid input. Please enter 'play' or 'menu'." + Style.RESET_ALL)


def main_menu():
    """Display the main menu and handle user selection."""
    clear()  # Clear the terminal at the start of the menu
    ascii_banner = pyfiglet.figlet_format("Welcome to Zodiac With Me")
    print(Fore.MAGENTA + ascii_banner + Style.RESET_ALL)

    print(Fore.CYAN + "Please choose an option:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Find Your Zodiac Sign" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Take a Zodiac Quiz" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Exit" + Style.RESET_ALL)

    while True:
        choice = input(Fore.CYAN + "\nEnter your choice (1/2/3): " + Style.RESET_ALL).strip()

        if choice == '1':
            zodiac_game()
            break
        elif choice == '2':
            zodiac_quiz()
            while True:
                play_again = input(Fore.YELLOW + "\nWould you like to take the quiz again or return to the main menu? (quiz/menu): " +
                                  Style.RESET_ALL).strip().lower()
                if play_again == 'quiz':
                    zodiac_quiz()
                    continue
                elif play_again == 'menu':
                    print(Fore.MAGENTA + "Returning to the main menu..." + Style.RESET_ALL)
                    main_menu()
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter 'quiz' or 'menu'." +
                          Style.RESET_ALL)
            break
        elif choice == '3':
            print(Fore.MAGENTA + "Returning to the main menu..." + Style.RESET_ALL)
            main_menu()  # Return to the main menu instead of exiting
        else:
            print(Fore.RED + "Invalid choice. Please select option 1, 2, or 3." +
                  Style.RESET_ALL)


if __name__ == "__main__":
    main_menu()
