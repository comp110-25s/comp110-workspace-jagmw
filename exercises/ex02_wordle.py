__author__ = "730580305"
# Emoji constants
WHITE_BOX: str = "\U00002B1C"  # ⬜
GREEN_BOX: str = "\U0001F7E9"  # 🟩
YELLOW_BOX: str = "\U0001F7E8"  # 🟨


def contains_char(text: str, character: str) -> bool:
    """Checks if a given single character is found in the provided text."""
    assert len(character) == 1, f"len('{character}') is not 1"

    for letter in text:
        if letter == character:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Compares a guess to the secret word and returns a string of emojis representing the accuracy."""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    emoji_result = ""

    # Check each character in the guess
    for i in range(len(guess)):
        if guess[i] == secret[i]:  # Correct letter and correct position
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):  # Correct letter, wrong position
            emoji_result += YELLOW_BOX
        else:  # Letter not in secret
            emoji_result += WHITE_BOX

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the expected length."""
    while True:
        guess = input(f"Enter a {expected_length} character word: ")

        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    turns = 6  # Maximum allowed turns
    current_turn = 1  # Start at turn 1
    has_won = False  # Track if user has won

    while current_turn <= turns and not has_won:
        print(f"=== Turn {current_turn}/{turns} ===")

        # Get user guess
        guess = input_guess(len(secret))

        # Display emoji results
        result = emojified(guess, secret)
        print(result)

        # Check if the guess is correct
        if guess == secret:
            has_won = True
            print(f"You won in {current_turn}/{turns} turns!")
        else:
            current_turn += 1

    if not has_won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
