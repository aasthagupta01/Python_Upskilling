import random
import string

class GreaterAlphabet(Exception):
    """entered alphabet is greater than predefined alphabet"""
    pass

class SmallerAlphabet(Exception):
    """entered alphabet is smaller than predefined alphabet"""
    pass

def guess_letter(alphabet: str):
    try:
        print("predefined letter is :", randomLetter)
        if alphabet > randomLetter:
            raise GreaterAlphabet

        elif alphabet < randomLetter:
            raise SmallerAlphabet

        else:
            print("you guessed the right alphabet")

    except SmallerAlphabet:
        print("Exception occured: Smaller alphabet entered")

    except GreaterAlphabet:
        print("Exception occured: Greater alphabet entered")

    return

if __name__ == "__main__":
    randomLetter = random.choice(string.ascii_letters)
    alphabet = input("guess the predefined alphabet:")
    guess_letter(alphabet)