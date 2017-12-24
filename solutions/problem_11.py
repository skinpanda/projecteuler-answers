# Title: Largest product in a grid

import os
from Module import Parser

AbsPath = os.path.abspath(os.path.dirname(__file__))
DataDir = AbsPath + "/resources/problem_11_data.txt"

DataArray = Parser(DataDir).str_to_array()  # Parse string data

for a in range(20):  # convert each string to integer
    DataArray[a] = [int(b) for b in DataArray[a]]


def compare(num, maxnum):
    if num > maxnum:
        maxnum = num
    return maxnum


Max = 0

for i in range(20):
    for j in range(20):
        if DataArray[i][j]:

            if i < 17:  # Down
                k = DataArray[i][j] * DataArray[i + 1][j] * DataArray[i + 2][j] * DataArray[i + 3][j]
                Max = compare(k, Max)
                if j > 2:  # Forward Diagonal
                    k = DataArray[i][j] * DataArray[i + 1][j - 1] * DataArray[i + 2][j - 2] * DataArray[i + 3][j - 3]
                    Max = compare(k, Max)

            if j < 17:  # Right
                k = DataArray[i][j] * DataArray[i][j + 1] * DataArray[i][j + 2] * DataArray[i][j + 3]
                Max = compare(k, Max)
                if i < 17:  # Backward Diagonal
                    k = DataArray[i][j] * DataArray[i + 1][j + 1] * DataArray[i + 2][j + 2] * DataArray[i + 3][j + 3]
                    Max = compare(k, Max)

print("Answer: ", Max)
