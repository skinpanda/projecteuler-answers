# Title: Large sum

import os
from Module import Parser


AbsPath = os.path.abspath(os.path.dirname(__file__))
DataDir = AbsPath + "/resources/problem_13_data.txt"
DataArray = Parser(DataDir).str_to_int()  # converts string list to integer

total = sum(DataArray)
first_ten = str(total)[:10]

print("Answer: ", first_ten)
