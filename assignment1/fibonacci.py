num = int(input("enter a range"))
first = 0
second = 1
count = 0
for i in range(num):
    sum = first+second
    print(first)
    first = second
    second = sum
