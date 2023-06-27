class reverse_iter:
    def __init__(self, input_list: list):
        self._list = input_list
        self._index = len(input_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            rev = self._list[self._index]
            self._index -= 1
            return rev

        else:
            raise StopIteration


if __name__ == "__main__":
    range_input = int(input("enter no of elements in list:"))
    input_list = []
    for i in range(range_input):
        element = int(input("enter elements in list:"))
        input_list.append(element)

    for a in reverse_iter(input_list):
        print(a)
