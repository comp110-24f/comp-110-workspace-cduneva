"""Challenge question 2"""

__author__ = "730653037"


global secret
secret = 7


def guess_a_number() -> None:
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    """If/else tree to decide response statements"""
    if int(guess) > int(secret):
        """if response too high"""
        print("Your guess was too high! The secret number is " + str(secret))
    elif int(guess) < int(secret):
        """if response too low"""
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(guess) == int(secret):
        """If response matches"""
        print("You got it!")
    else:
        """in case of error"""
        print("Invalid guess, please try again")

    return None


if __name__ == "__main__":
    """calling the main function to begin the program"""
    guess_a_number()
