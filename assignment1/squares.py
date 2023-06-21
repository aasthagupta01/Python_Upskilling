"""function to return list of squares of input list of numbers"""
def squares() -> list:
    list_of_squares = []
    input_num = int(input("enter number of elements you want to enter"))
    for num in range(input_num):
        element = int(input("enter element into list"))
        list_of_squares.append(element**2)
    return list_of_squares

if __name__ == "__main__":
    print(f"list of squares of elements is {squares()}")
