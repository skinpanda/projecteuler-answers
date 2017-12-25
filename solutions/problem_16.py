# Title: Power digit sum

# Convert the equivalent of 2^1000 to string
result_string = str(2**1000)

# Loop through the string
result_length = len(result_string)
sum_digits = 0

for i in range(result_length):
    sum_digits += int(result_string[i])

print("Answer: ", sum_digits)
