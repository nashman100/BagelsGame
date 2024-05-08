import random

digits = 3
max_guesses = 10


def main():
    print('''
    I am thinking of a three digit number. Try and guess what it is. You have 10 guesses!
    When I say:     That Means:      
    Pico            One Digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No Digit is correct.      

    For example if the number was 123 and your guess was 321, the clues would be Fermi Pico.''')

    while True:
        secret = gen_number()
        print("I have chosen a number")
        print(secret)
        print("You have {} guesses left".format(max_guesses))
        num_guesses = 0
        guesses_left = max_guesses
        while num_guesses < max_guesses:
            guess = input("Guess a number: ")
            if not guess.isdigit() or len(guess) != digits:
                print("Please enter a {} digit number".format(digits))
                continue
            clues = check_guess(guess, secret)
            print("Clues: " + clues)
            num_guesses += 1
            guesses_left -= 1
            if clues == "Congrats! You guessed the correct number.":
                print("Congrats! You guessed the number in {} guesses.".format(num_guesses))
                break
            print("You have {} guesses left.".format(guesses_left))
        else:
            print("Sorry you ran out of guesses. The number was {}".format(secret))

        replay = input("Do you want to play again? (Y/N): ").strip().upper()
        if replay != "Y":
            print("Thank you for playing!")
            break


def gen_number():

    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ""

    for i in range(digits):
        secret_number += str(numbers[i])
    return secret_number


def check_guess(guess, secret_number):

    clues = []

    if guess == secret_number:
        return "Congrats! You guessed the correct number."

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == '__main__':
    main()