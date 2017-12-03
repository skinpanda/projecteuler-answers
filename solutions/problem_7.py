# Title: 10001st prime

from itertools import count
import math


PrimeCount = 2  # 2 and 3 are already counted

# Test for primality (from 2 to sqrt(i))

for i in count(5, 2):
    IsPrime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            IsPrime = False
            break
  
    if IsPrime:
        PrimeCount += 1
    if PrimeCount == 10001:
        break
  
print("Answer: ", i)
