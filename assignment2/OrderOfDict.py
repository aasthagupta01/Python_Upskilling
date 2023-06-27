import collections
class OrderedDict:
    def __init__(self):
        self.dict = {}
        self.keys = []

    def insert(self, key, value):
        if key not in self.dict:
            self.keys.append(key)
            self.dict[key] = value

    def delete(self, key):
        if key in self.dict:
            self.keys.remove(key)
            del self.dict[key]
        else:
            return "key not in dictionary"

    def get(self, key):
        return self.dict.get(key)

    def get_ordered_keys(self):
        return self.keys

    def get_ordered_values(self):
        return [self.dict[key] for key in self.keys]

    def display(self):
        return self.dict

if __name__ == "__main__":
    input_dict = OrderedDict()
    input_dict.insert('a', 1)
    input_dict.insert('b', 2)
    input_dict.insert('c', 3)
    input_dict.insert('d', 4)
    print(f"dictionary is {input_dict.display()}") #print the dictionary

    value1 = input_dict.get('a')
    print(value1) #print value of a specific key
    input_dict.delete('c')    #deleting a key

    ordered_keys = input_dict.get_ordered_keys()
    ordered_values = input_dict.get_ordered_values()
    print(ordered_keys)
    print(ordered_values)