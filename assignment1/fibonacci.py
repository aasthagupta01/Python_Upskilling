num = int(input("How many fibonacci numbers to generate?"))
first = 0
second = 1
sum=0
for i in range(num):
    sum = first+second
    print(first)
    # swapping the numbers
    first = second
    second = sum
