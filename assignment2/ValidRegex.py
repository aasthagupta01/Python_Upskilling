import re


# using re module

def valid_regex(string: str):
    try:
        re.compile(string)
        return True

    except re.error:
        return False


string = input("Enter a string to check valid regex or not")
if valid_regex(string) == True:
    print(string, "is valid regex")

else:
    print(string, "is not a valid regex")
