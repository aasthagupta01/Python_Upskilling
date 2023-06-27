"""It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4 , separated by one hyphen "-".
► It must NOT use any other separator like '  ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""
import re
class ShortLength(Exception):
    """does not match the card limit i.e. 16"""
    pass

class ExceedsLength(Exception):
    """exceeds the card limit i.e. 16"""
    pass

class RepeatedDigits(Exception):
    """it has 4 or more consecutive repeated digits"""
    pass

"""function to count occurrences of digits in card number"""
def count_occurrence(card_no: str) -> bool:
    list_of_card_no = list(card_no.replace('-', ''))
    count = 1
    if len(list_of_card_no) > 16:
        raise ExceedsLength
    elif len(list_of_card_no) < 16:
        raise ShortLength

    else:
        for digit in range(0, len(list_of_card_no) - 1):
            if list_of_card_no[digit] == list_of_card_no[digit + 1]:
                count += 1
                if count >= 4:
                    raise RepeatedDigits
            else:
                count = 1

    return True


"""function to validate card number with all the given conitions"""
def validate_credit_card_num(num: str) -> str:
    try:
        if count_occurrence(num):
            regex = re.compile(r'(^[456]\d{3})-(\d{4})-(\d{4})-(\d{4}$)')
            if regex.search(num):
                return f"{num} is valid"

            else:
                return f"{num} is invalid"

    except ExceedsLength:
        return "card number consist of more than 16 digits"

    except RepeatedDigits:
        return "card number has 4 or more consecutive repeated digits"


if __name__ == "__main__":
    card_num = input("enter card number:")
    print(validate_credit_card_num(card_num))
