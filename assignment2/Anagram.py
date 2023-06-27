import random

"""function returns a random word from a list of words whose anagrams are present"""
def give_word_for_anagram() -> str:
    words = ['race', 'heart', 'listen', 'loop', 'sore']
    # randomly choosing a word from list of anagrams
    anagram = random.choice(words)
    return anagram

"""a function to guess the right anagram for the given word"""
def guess_anagram(anagram: str):
    for num in range(1, len(anagram) + 1):
        guess_word = input("guess an anagram for the word")
        if sorted(anagram) == sorted(guess_word):
            print(f"You guessed it RIGHT! {guess_word} is anagram of {anagram}")
            break
        else:
            print(f"You guessed it WRONG! You have now {len(anagram) - num} chances left")

if __name__ == "__main__":
    anagram = give_word_for_anagram()
    print(f"give anagram for word:{anagram}")
    print(f"you have {len(anagram)} number of chances")
    guess_anagram(anagram)
