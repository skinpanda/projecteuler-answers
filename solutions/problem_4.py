# Title: Largest palindrome product


# palindrome returns true if n is palindrome


def palindrome(n):
    n = str(n)              # convert n to string
    return n == n[::-1]     # check if n is same as reversed n


product, lower_multiple = set(), {0}  # use set for faster calculations

for x in range(999, 99, -1):
    if x <= max(lower_multiple):
        break
    for y in range(x, 99, -1):
        if palindrome(x*y):
            product.add(x*y)
            lower_multiple.add(y)

print(max(product))
