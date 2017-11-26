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

<<<<<<< HEAD
print("Answer: ", sum(fibonacci[2::3]))

=======
print(sum(fibonacci[2::3]))
>>>>>>> c3302207fa270afa894dc2b7480290ec691251a6
