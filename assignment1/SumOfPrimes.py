def prime_numbers(input_num: int) -> list:
    list_of_primes = []
    for num in range(2, input_num + 1):
        count = 0
        for j in range(2, num):
            if num % j == 0:
                count += 1
            else:
                continue
        if count == 0:
            list_of_primes.append(num)
        else:
            continue

    return list_of_primes

if __name__ == "__main__":
    prime_nums = prime_numbers(100)
    print(f"sum is: {sum(prime_nums)}")
