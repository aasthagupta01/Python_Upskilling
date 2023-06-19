"""program to find the reverse of a user given number."""


def reverse(num: int) -> int:
    rev = 0

    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num = num // 10

    return rev


num = int(input("enter a number:"))
print("original number is:", num)
print("reverse of number is:", reverse(num))
