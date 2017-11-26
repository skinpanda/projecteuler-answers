# Even Fibonacci Numbers
import time


def fibonacci_sequence(limit):
    fibonacci_list = []
    a, b = 0, 1
    while b < limit:
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list


fibonacci = fibonacci_sequence(4000000)
print(sum(fibonacci[2::3]))

