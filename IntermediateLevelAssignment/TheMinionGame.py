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

def minion_game(string: str) -> str:
    try:
        new_list = []
        pointsv = 0
        pointsc = 0
        if all(c.isupper() for c in string):
            for index in range(len(string)):
                for num in range(index + 1, len(string) + 1):
                    new_list.append(string[index:num])

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


if __name__ == "__main__":
    input_str = input("enter a string:")
    print(minion_game(input_str))

