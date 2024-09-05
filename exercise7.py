# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    fixed_num = 27
    total_attempts = 5
    
    for attempt in range(1, total_attempts + 1):
        user_guess = input(f'Attempt {attempt}: guess a number between (1-100): ')
        
        if not user_guess.isdigit():
            print('please enter a number')
            continue
        
        user_guess = int(user_guess)
        
        if user_guess < 1 or user_guess > 100:
            print('Please enter a valid guess.')
            continue
        
        if user_guess == fixed_num:
            print('Congratulations, you guessed correctly!')
            break
        elif user_guess < fixed_num:
            if attempt < total_attempts:
                print('Guess is too low')
        elif user_guess > fixed_num:
            if attempt < total_attempts:
                print('Guess is too high.')
        
        if attempt == 4:
            print('Last Chance')
        if attempt == total_attempts:
            if user_guess != fixed_num:
                print(f'Sorry, you failed to guess the number in {total_attempts} attempts.')
    

# Call the function
guess_number()