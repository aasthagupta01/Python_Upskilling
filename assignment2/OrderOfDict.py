input_dict = {}
num = int(input("enter how many key value pairs you want to enter:"))

for i in range(num):
    key = input("enter a key:")
    value = input("enter a value")
    input_dict[key] = value

# converting dictionary into list to perform sorting
list_of_dict = list(input_dict)

# sorting the list of keys of dictionary
list_of_dict.sort()

# converting sorted list back to dictionary by method 1
sorted_dict = {}
for keys in list_of_dict:
    sorted_dict[keys] = input_dict[keys]
print(sorted_dict)

# converting sorted list back to dictionary by method 2
sorted_dict = {i: input_dict[i] for i in list_of_dict}
print(sorted_dict)
