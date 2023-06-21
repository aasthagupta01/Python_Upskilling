"""program to find the reverse of a user given number."""
def reverse(num: int) -> int:
    rev = 0

    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num = num // 10

    return rev

if __name__ == "__main__":
    num = int(input("enter a number:"))
    print(f"original number is: {num}")
    print(f"reverse of number is: {reverse(num)}")
