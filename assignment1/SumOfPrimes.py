
def sum_of_primes(num):
    sum = 17
    for i in range(11, num):
        for j in range(2, int(i/2) +1):
            if i % j != 0:
                sum += i
    return sum

print("sum is:", sum_of_primes(200000))
