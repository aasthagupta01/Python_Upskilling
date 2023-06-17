# printing list of squares using for loop

list_of_num = [1, 2, 3, 4, 5]
squares = []
for num in list_of_num:
    squares.append(num ** 2)
print(squares)

'''printing list of squares using list comprehensions'''
list_of_square = [var ** 2 for var in range(1, 6)]
print(list_of_square)
