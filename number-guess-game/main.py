import random

print("Welcome to the Number Game! This is a number guessing game!\nYou have only 5 attempts to guess the number between 50 to 100. Let's start the game!")

number_to_guess = random.randint(50, 100)
chances = 5  
guess_count = 0  

while guess_count < chances:
    my_guess = int(input("Please enter your guess: "))
    guess_count += 1 

    if my_guess == number_to_guess:
        print(f"Congratulations! The number is {number_to_guess} and you guessed it in {guess_count} attempts.")
        break
    elif my_guess < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    if guess_count == chances:
        print(f"Oops! You've used all attempts. The number was {number_to_guess}. Better luck next time!")
