"""Comp110 Wordle Exercise"""

__author__: str = "730653037"


def input_guess(secret_word_len: int) -> str:
    """Prompts user for a guess and checks if it has the correct length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, character_to_find: str) -> bool:
    """Defines function with the 2 parameters being search string and search character"""
    assert len(character_to_find) == 1
    index = 0
    while index < len(secret_word):
        if secret_word[index] == character_to_find:
            return True
        index += 1
    return False


def emojified(secret_word: str, guess: str) -> str:
    assert len(secret_word) == len(guess)
    """ensuring the length of the secret word is the same as the guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    """Setting the constant for the emoji boxes"""
    emoji_string = ""
    i = 0
    """creates the emoji string list and sets the index at 0"""
    while i < len(secret_word):
        if secret_word[i] == guess[i]:
            emoji_string += GREEN_BOX
        elif contains_char(secret_word, guess[i]) and secret_word[i] != guess[i]:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
            """adds white boxed for failed guesses"""
        i += 1
        """adds 1 to the index to reset the loop"""

    return emoji_string


"""ends the loop"""


def main(secret_word: str) -> None:
    """The main function."""
    turns = 6
    current_turn = 1
    while current_turn <= turns:
        print(f"=== Turn {current_turn}/6 ===")
        guess = input_guess(len(secret_word))

        print(emojified(secret_word, guess))  # Call emojified here

        if guess == secret_word:
            print(f"You won in {current_turn}/6 turns!")
            break
        else:
            current_turn += 1

    if current_turn > turns:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
