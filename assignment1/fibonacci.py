"""function to generate fibonacci series until a given num
returns list of fibonacci numbers"""
def fibonacci_series(num: int) -> list:
    first = 0
    second = 1
    sum = 0
    list_of_fib_nums = []
    for i in range(num):
        sum = first + second
        list_of_fib_nums.append(first)
        # swapping the numbers
        first, second = second, sum

    return list_of_fib_nums

if __name__ == "__main__":
    num = int(input("How many fibonacci numbers to generate?"))
    fib_nums = fibonacci_series(num)
    print(f"fibonacci series is: {fib_nums}")
