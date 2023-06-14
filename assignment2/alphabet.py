import random
import string

randomLetter = random.choice(string.ascii_letters)

alphabet = input("guess the predefined alphabet:")

class greaterAlphabet(Exception):
    print("entered alphabet is greater than predefined alphabet")


class smallerAlphabet(Exception):
    print("entered alphabet is smaller than predefined alphabet")


try:
    print("predefined letter is :",randomLetter)
    if alphabet>randomLetter:
        raise Exception

    elif alphabet<randomLetter:
        raise Exception

    else:
        print("you guessed the right alphabet")


finally:
    print("you enterred",alphabet)