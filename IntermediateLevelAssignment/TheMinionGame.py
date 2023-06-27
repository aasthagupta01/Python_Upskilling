import re
class HasDigit(Exception):
    """input string contains numbers. not allowed"""
    pass

class HasLowerAlpha(Exception):
    """input string contains lower alphabets. Only upper case alphabets allowed"""
    pass

class InvalidInput(Exception):
    """invalid input"""
    pass

"""def minion_game(l: list):
    vowels = "AEIOU"
    words_starting_with_vowels = []
    words_starting_with_cons = []

    for words in l:
        if words[0] in vowels:
            words_starting_with_vowels.append(words)
        else:
            words_starting_with_cons.append(words)

    return list(set(words_starting_with_vowels)), list(set(words_starting_with_cons))
"""

# return list(set(words_starting_with_cons))
def minion_game(string: str) -> str:
    try:
        new_list = []
        pointsv = 0
        pointsc = 0
        if all(c.isupper() for c in string):
            for i in range(len(string)):
                for w in range(i + 1, len(string) + 1):
                    new_list.append(string[i:w])

            for words in new_list:
                if words[0] in "AEIOU":
                    pointsv += 1

                else:
                    pointsc += 1

            if pointsc > pointsv:
                return f"Stuart {pointsc}"
            elif pointsc == pointsv:
                return "Draw"
            else:
                return f"Kevin {pointsv}"""

        elif re.search(r'\d',string):
            raise HasDigit

        elif re.search("[a-z]",string):
            raise HasLowerAlpha

        else:
            raise InvalidInput

    except HasLowerAlpha:
        return "input string contains lower alphabets. not allowed"

    except HasDigit:
        return "input string contains numbers. not allowed"

    except InvalidInput:
        return "invalid input"


"""def count_points(listsubs: list, fullstring: str) -> int:
    sum = 0
    for word in listsubs:
        count = fullstring.count(word)
        sum += count
    return sum"""


"""def game_result(points1: int, points2: int):
    if points1 > points2:
        return f"Stuart {points_of_stuart}"
    elif points1 == points2:
        return "Draw"
    else:
        return f"Kevin {points_of_kevin}"""

if __name__ == "__main__":
    input_str = input("enter a string:")
    #list_of_substr = substring(input_str)
    print(minion_game(input_str))

