import random

words = ['race', 'heart', 'listen', 'loop', 'sore']

anagram = random.choice(words)
length = len(anagram)
print("the word is :", anagram)
print("you have", length, "number of chances")

for i in range(1, length + 1):
    guess_word = input("guess an anagram for the word")

    if sorted(anagram) == sorted(guess_word):
        print("You guessed it RIGHT!", guess_word, "is anagram of", anagram)
        break

    else:
        print("You guessed it WRONG! You have now", length - i, "chances left")
