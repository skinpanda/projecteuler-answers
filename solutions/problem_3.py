# Title: Largest prime factor

# Test for factors starts at 3 since all even factors will
# be removed first (Loop: Remove even factors)
number = 600851475143
factor = 3

# Loop: Remove even factors
while number % 2 == 0:
    number /= 2

# While loop makes sure all multiples of each factor is removed
# Remember that the only even prime factor is 2
while number != 1:
    val = number / factor
    if val.is_integer():
        number = val
    else:
        factor += 2  # test all odd factors starting at 3

print("Answer: ", factor)
