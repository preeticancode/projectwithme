import sys
from datetime import datetime
import pyfiglet
from colorama import init, Fore, Style
import os
import random

# Initialize colorama for color support
init()

# Clear function to clean up the terminal
def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Function to get the zodiac sign based on the birthdate
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", "Courageous, determined, and confident."
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", "Reliable, patient, and devoted."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", "Gentle, affectionate, and curious."
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", "Tenacious, highly imaginative, and loyal."
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", "Creative, passionate, and cheerful."
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", "Loyal, analytical, and hardworking."
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", "Cooperative, diplomatic, and fair-minded."
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", "Resourceful, brave, and passionate."
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", "Generous, idealistic, and great sense of humor."
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", "Responsible, disciplined, and self-control."
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", "Progressive, original, and independent."
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces", "Compassionate, artistic, and intuitive."
    
    return None, None

# Function to ask a Zodiac quiz
def zodiac_quiz():
    clear()  # Clear the terminal before starting the quiz
    print(Fore.CYAN + "\nZodiac Quiz: Let's see how well you know the Zodiac signs!" + Style.RESET_ALL)
    
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
        answer = input(Fore.YELLOW + question + " ").lower().strip()
        if answer == correct_answer:
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer was {correct_answer.capitalize()}." + Style.RESET_ALL)
    
    print(Fore.CYAN + f"\nYou got {score} out of {len(selected_questions)} correct!" + Style.RESET_ALL)

# Function to find the zodiac sign based on birthdate
def zodiac_game():
    clear()  # Clear the terminal at the start of the game
    print(Fore.CYAN + "Please enter your birthdate to find out your zodiac sign." + Style.RESET_ALL)
    
    # Get user's birthdate
    birthdate_str = input(Fore.YELLOW + "Enter your birthdate (YYYY-MM-DD): " + Style.RESET_ALL)
    
    # Convert the input to a date object
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "Invalid date format. Please enter the date in YYYY-MM-DD format." + Style.RESET_ALL)
        return
    
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
    
    # Ask if the user wants to play again or exit
    play_again = input(Fore.YELLOW + "\nWould you like to play again or exit? (play/exit): " + Style.RESET_ALL).strip().lower()
    if play_again == 'play':
        main_menu()
    else:
        print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
        sys.exit()

# Main menu function
def main_menu():
    clear()  # Clear the terminal at the start of the menu
    # Use pyfiglet to create a fancy welcome message
    ascii_banner = pyfiglet.figlet_format("Welcome to Zodiac With Me")
    print(Fore.MAGENTA + ascii_banner + Style.RESET_ALL)
    
    print(Fore.CYAN + "Please choose an option:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Find Your Zodiac Sign" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Take a Zodiac Quiz" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Exit" + Style.RESET_ALL)
    
    choice = input(Fore.CYAN + "\nEnter your choice (1/2/3): " + Style.RESET_ALL).strip()
    
    if choice == '1':
        zodiac_game()
    elif choice == '2':
        zodiac_quiz()
        # After the quiz, ask if the user wants to play again or exit
        play_again = input(Fore.YELLOW + "\nWould you like to play again or exit? (play/exit): " + Style.RESET_ALL).strip().lower()
        if play_again == 'play':
            main_menu()
        else:
            print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            sys.exit()
    elif choice == '3':
        print(Fore.MAGENTA + "Thanks for visiting! Goodbye!" + Style.RESET_ALL)
        sys.exit()
    else:
        print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)
        main_menu()

if __name__ == "__main__":
    main_menu()

