import re

"""a function to check if entered string is valid regex or not
return True or False"""
def valid_regex(string: str)-> bool:
    try:
        re.compile(string)
        return True

    except re.error:
        return False

if __name__ == "__main__":
    string = input("Enter a string to check valid regex or not")
    if valid_regex(string) == True:
        print(f"{string} is valid regex")
    else:
        print(f"{string} is not a valid regex")
