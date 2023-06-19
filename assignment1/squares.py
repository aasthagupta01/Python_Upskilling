# printing list of squares

def squares() -> list:
    list_of_squares = []
    num = int(input("enter number of elements you want to enter"))
    for i in range(num):
        element = int(input("enter element into list"))
        list_of_squares.append(element ** 2)
    return list_of_squares


print("list of squares of elements is", squares())

