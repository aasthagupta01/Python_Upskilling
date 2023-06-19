def sum_of_primes(num):
    sum = 0
    for i in range(2, num + 1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1

            else:

                continue
        if count == 0:
            sum += i
        else:
            continue

    return sum

print("sum is:", sum_of_primes(200000))
