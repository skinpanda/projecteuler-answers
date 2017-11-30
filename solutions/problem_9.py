# Title: Special Pythagorean triplet

# Pythagorean triplet members a, b and c are always
# in multiple of 3, 4 and 5 respectively

for i in range(3, 500, 3):
    for j in range(4, 500, 4):
        c = 1000 - i - j
        if (i ** 2) + (j ** 2) == c**2:
            print("Answer: ", i * j * c)
