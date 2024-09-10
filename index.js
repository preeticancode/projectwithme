import sys
from datetime import datetime
import random
import pyfiglet
import os


def clear():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


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


# Zodiac sign game function
def zodiac_sign_game():
    while True:
        print("Please enter your birthdate to find out your zodiac sign.")
        
        # Get user's birthdate
        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()

        # Convert the input to a date object
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.\n")
            retry = input("Would you like to retry? (yes/no): ").strip().lower()
            if retry == 'yes':
                continue
            else:
                print("Thanks for playing! Goodbye!")
                return
        
        # Get day and month from the birthdate
        day = birthdate.day
        month = birthdate.month

        # Determine the zodiac sign
        sign, description = get_zodiac_sign(day, month)

        if sign:
            print(f"\nYour zodiac sign is {sign}!")
            print(f"Description: {description}\n")
        else:
            print("Sorry, we couldn't determine your zodiac sign. Please try again.")
        
        play_again = input("\nWould you like to retry? (yes/no): ").strip().lower()
        if play_again == 'no':
            print("Thanks for playing! Goodbye!")
            break
        elif play_again != 'yes':
            print("Please select a valid option.")
        else:
            continue


# Zodiac quiz function
def zodiac_quiz():
    questions = [
        {"question": "Which element is associated with Aries?", "answer": "Fire"},
        {"question": "Which zodiac sign is known for being diplomatic?", "answer": "Libra"},
        {"question": "Which sign is ruled by the planet Venus?", "answer": "Taurus"},
        {"question": "What is the symbol of Gemini?", "answer": "Twins"},
        {"question": "What sign is represented by the lion?", "answer": "Leo"},
        {"question": "Which sign is known for its emotional depth?", "answer": "Scorpio"},
        {"question": "Which sign is associated with being adventurous?", "answer": "Sagittarius"},
        {"question": "Which element is associated with Pisces?", "answer": "Water"},
        {"question": "Which sign is considered the most analytical?", "answer": "Virgo"},
        {"question": "What is the symbol for Cancer?", "answer": "Crab"}
    ]

    score = 0
    random.shuffle(questions)
    
    for i, question in enumerate(questions[:5]):
        print(f"Question {i + 1}: {question['question']}")
        
        user_answer = input("Your answer: ").strip()

        # Validate if the input is not blank
        while not user_answer:
            print("Answer cannot be blank. Please enter a valid answer.")
            user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question['answer']}.\n")
    
    print(f"Your final score is {score}/5.")

    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        zodiac_quiz()
    else:
        print("Thanks for playing! Goodbye!")


# Main menu function
def main_menu():
    ascii_banner = pyfiglet.figlet_format("Welcome to Zodiac With Me")
    print(ascii_banner)
    
    while True:
        print("Main Menu:")
        print("1. Zodiac Sign Game")
        print("2. Zodiac Quiz")
        print("3. Exit")

        choice = input("Please select an option (1/2/3): ").strip()

        if choice == "1":
            zodiac_sign_game()
        elif choice == "2":
            zodiac_quiz()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please select a valid option (1, 2, or 3).\n")


if __name__ == "__main__":
    clear()
    main_menu()
