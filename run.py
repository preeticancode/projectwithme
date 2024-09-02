import sys
from datetime import datetime
import pyfiglet

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

# Main game loop function
def play_zodiac_game():
    # Use pyfiglet to create a fancy welcome message
    ascii_banner = pyfiglet.figlet_format("Welcome to Zodiac With Me")
    print(ascii_banner)
    
    print("Please enter your birthdate to find out your zodiac sign.")
    
    # Get user's birthdate
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    
    # Convert the input to a date object
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    
    # Get day and month from the birthdate
    day = birthdate.day
    month = birthdate.month
    
    # Determine the zodiac sign
    sign, description = get_zodiac_sign(day, month)
    
    if sign:
        print(f"\nYour zodiac sign is {sign}!")
        print(f"Description: {description}")
    else:
        print("Sorry, we couldn't determine your zodiac sign. Please try again.")
    
    # Ask if the user wants to play again
    play_again = input("\nWould you like to find another zodiac sign? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_zodiac_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_zodiac_game()
