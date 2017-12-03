# Title: Summation of primes

import math


PrimeSum = 5  # 2 and 3 are already counted

# Test for primality (from 2 to sqrt(i))

for i in range(5, 2000000, 2):
    IsPrime = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            IsPrime = False
            break

    if IsPrime:
        PrimeSum += i

print("Answer: ", PrimeSum)
