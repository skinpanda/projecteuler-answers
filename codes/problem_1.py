# Title: Multiples of 3 and 5

# Create set of multiples of 3 and 5
multiples = set(range(0, 1000, 3)) | set(range(0, 1000, 5))

print(sum(list(multiples)))
