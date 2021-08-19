#simple one player number guesing game

n = 23
number_of_guesses = 1
print("YOU HAVE ONLY 5 NUMBER OF GUESSES TO GUESS THE NUMBER: ")
while (number_of_guesses <= 5):
    guess_number = int(input("GUESS THE NUMBER :\n"))
    if guess_number < 23:
        print("ENTERED NUMBER IS SMALLES ,SELECT BIGGER NUMBER.\n")
    elif guess_number > 23:
        print("ENTERED NUMBER IS BIGGER ,SELECT SMALLER NUMBER.\n ")
    else:
        print("CONGRATULATIONS.....U WON!!!!!\n")
        print("U TOOK",number_of_guesses," NUMBER OF GUESSES TO CORRECTLY GUESS THE NUMBER")
        break
    print(5 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 5):
    print("Game Over")
    
 ------------------------------------------------------------------------------------------------------------
#two player number guessing game
import random

def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g1 > g2:
        print("Player 2 won the match!\n")

    else:
        print("Its a Tie!\n")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")
