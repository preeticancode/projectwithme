import sys
from datetime import datetime
import pyfiglet
from colorama import init, Fore, Style
import os

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
        "Which Zodiac sign is the most artistic?": "pisces"
    }
    
    score = 0
    for question, correct_answer in questions.items():
        answer = input(Fore.YELLOW + question + " ").lower().strip()
        if answer == correct_answer:
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer was {correct_answer.capitalize()}." + Style.RESET_ALL)
    
    print(Fore.CYAN + f"\nYou got {score} out of {len(questions)} correct!" + Style.RESET_ALL)

# Main game loop function
def play_zodiac_game():
    clear()  # Clear the terminal at the start of the game
    # Use pyfiglet to create a fancy welcome message
    ascii_banner = pyfiglet.figlet_format("Welcome to Zodiac With Me")
    print(Fore.MAGENTA + ascii_banner + Style.RESET_ALL)
    
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
    
    # Ask if the user wants to take the quiz
    take_quiz = input(Fore.YELLOW + "\nWould you like to take a Zodiac quiz? (yes/no): " + Style.RESET_ALL).strip().lower()
    if take_quiz == 'yes':
        zodiac_quiz()
    
    # Ask if the user wants to play again
    play_again = input(Fore.YELLOW + "\nWould you like to find another zodiac sign? (yes/no): " + Style.RESET_ALL).strip().lower()
    if play_again == 'yes':
        play_zodiac_game()
    else:
        print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    play_zodiac_game()
