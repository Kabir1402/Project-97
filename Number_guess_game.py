# random number generator
import random


secret_number = random.randint(1, 9)
guess_count = 1
guess_limit = 5
# main program number guessing game
print(f"your number is between {1} and {9} , Try guessing it .")

while guess_count < guess_limit:
    print(f"you have {guess_limit + 1 -guess_count} more guesses to find the secret number")
    guess = int(input("Guess: "))
    guess_count = guess_count + 1
    if guess == secret_number:
        print("you got the right number!")
        break
    elif guess > secret_number:
        print(f"try again, Guess lower ")

    elif guess < secret_number:
        print(f"try again, Guess higher ")


else:
    print(f"you lost the answer is {secret_number} ")
