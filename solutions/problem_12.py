# Title: Highly divisible triangular number

from functools import reduce
import operator
from itertools import count


def prod(iterable):  # returns product of list elements
    return reduce(operator.mul, iterable, 1)


def tri(n):  # returns nth triangular number
    return sum(range(n+1))


# Number of divisors is the sum of power of prime numbers of that number (add 1 to each power)
# For explanation, see: https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html

def divisor(number):  # returns number of divisors
    factor = 3
    a = []
    two = 0
    odd = 0

    while number % 2 == 0:
        number /= 2
        two += 1

    a.append(two + 1)

    while number != 1:
        val = number / factor
        if val.is_integer():
            number = val
            odd += 1
        else:
            a.append(odd + 1)
            odd = 0
            factor += 2
        if number == 1:
            a.append(odd + 1)

    return prod(a)


for j in count(1):  # start from 1
    TriangularNum = tri(j)
    if divisor(TriangularNum) > 500:
        print("Answer: ", TriangularNum)
        break
