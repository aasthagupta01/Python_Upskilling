""" this function removes duplicate values from the user input list """
def input_list_from_user() -> list:
    list_of_elements = []
    num = int(input("enter number of elements you want to enter"))
    for i in range(num):
        element = input("enter element into list")
        list_of_elements.append(element)
    return list_of_elements

if __name__ == "__main__":
    user_list = input_list_from_user()
    # Following statement uses `set` to remove duplicates
    refined_user_list = set(user_list)
    print(f"new list after removing duplicates is: {list(refined_user_list)}")