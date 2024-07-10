import random
from art import logo
print(logo)

def game_og():
    guessed_number = random.randint(1, 100)

    # Asking for user input
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    def game():
        def lvl():
            lvl = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
            return lvl

        l = lvl()

        def making_a_guess():
            x = input("Make a guess: ")
            return x

        def determining():
            if l == 'easy':
                lives = 11
            elif l == 'hard':
                lives = 6
            while lives >= 1:
                lives -= 1
                if lives == 0:
                    print("You ran out of lives!")
                    print("Better luck next time!")
                    break
                else:
                    print(f"You have {lives} lives left.")
                    y = int(making_a_guess())
                    if y == guessed_number:
                        print(f"You got it! The answer was {y}")
                        break
                    elif y != guessed_number:
                        if y > guessed_number:
                            print("Too High!")
                            print("Guess again")
                        elif y < guessed_number:
                            print("Too low")
                            print("Guess again")

        if l == "easy" or l == 'hard':
            determining()
        else:
            print("Please enter a valid difficulty input.")
            game()

    game()

game_og()

wanna = input("Do you wanna play again? Type 'Yes' or 'No: ").strip().lower()

if wanna == 'yes':
    game_og()
else:
    exit()
