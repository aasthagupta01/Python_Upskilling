import random
import string

# generates a random letter form a-z
randomLetter = random.choice(string.ascii_letters)
alphabet = input("guess the predefined alphabet:")


class GreaterAlphabet(Exception):
    """entered alphabet is greater than predefined alphabet"""
    pass


class SmallerAlphabet(Exception):
    """entered alphabet is smaller than predefined alphabet"""
    pass


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

finally:
    print("you entered", alphabet)
