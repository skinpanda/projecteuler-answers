# Title: Largest product in a series

import os

# Open file containing data

AbsPath = os.path.abspath(os.path.dirname(__file__))
File = open(AbsPath + "/resources/problem_8_data.txt", "r")

with File as f:
    Number = "".join([num.replace("\n", "") for num in f])  # remove newline character

LargestProduct = 0

for i in range(0, 987):
    Product = 1
    for j in range(i, i + 13):
        Product *= int(Number[j])
    if Product > LargestProduct:
        LargestProduct = Product

print("Answer: ", LargestProduct)
