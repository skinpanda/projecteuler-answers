# Title: Even Fibonacci Numbers


# Generate a list of Fibonacci numbers less than <limit>
# Returns [1, 1, 2, 3, ...]


def fibonacci_sequence(limit):
    fibonacci_list = []
    a, b = 0, 1
    while b < limit:
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list


fibonacci = fibonacci_sequence(4000000)

# Even Fibonacci Numbers appear on every third iteration
# First even Fibonacci number is 2 at fibonacci_list[2] (third on the list)
# Hence the list slicing [2::3]

print("Answer: ", sum(fibonacci[2::3]))
