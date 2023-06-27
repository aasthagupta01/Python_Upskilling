"""Program to sort the string with alphanumeric characters only(With Unit test cases). Sorting requires:
► All sorted lowercase letters are ahead of uppercase letters.
► All sorted uppercase letters are ahead digits.
► All sorted odd digits are ahead of sorted even digits.
"""
class NotAlphanum(Exception):
    """not an alphanumeric string"""
    pass

"""method to sort an alphanumeric string 
returns the sorted string"""
def alphanumeric_sorting(alphanum: str) -> str:
    try:
        lower_alpha = []
        upper_alpha = []
        odd_digit = []
        even_digit = []

        for i in alphanum:
            if i.isalnum():
                if i.isalpha():
                    if i.islower():
                        lower_alpha.append(i)

                    elif i.isupper():
                        upper_alpha.append(i)

                if i.isdigit():
                    if int(i) % 2 != 0:
                        odd_digit.append(i)

                    else:
                        even_digit.append(i)

            else:
                raise NotAlphanum

        #sorting the above created lists
        lower_alpha.sort()
        upper_alpha.sort()
        odd_digit.sort()
        even_digit.sort()

        #using join() method to convert list to string as well as join all the lists and returning the sorted string
        sorted_str = ''.join(lower_alpha) + ''.join(upper_alpha) + ''.join(odd_digit) + ''.join(even_digit)
        return sorted_str

    except NotAlphanum:
        return "not a valid alphanumeric string."

if __name__ == '__main__':
    alphanumeric_string = input("enter the alphanumeric string:")
    print(f"sorted alphanumeric string is {alphanumeric_sorting(alphanumeric_string)}")


