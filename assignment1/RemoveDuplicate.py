""" this function removes duplicate values from the user input list """


def remove_duplicate() -> list:
    list_of_elements = []
    num = int(input("enter number of elements you want to enter"))
    for i in range(num):
        element = input("enter element into list")
        list_of_elements.append(element)
    print("original list is", list_of_elements)

    new_list = []
    for i in list_of_elements:
        if i not in new_list:
            new_list.append(i)

    return new_list


print("new list is", remove_duplicate())
