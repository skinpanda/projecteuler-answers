# Title: Lattice Paths

from Module import Pascal

# Problem can be solved using Pascal's triangle
# Number of routes lies on (number_of_grid*2)th line of the Pascal triangle
# From the example, number_of_grid is 2, number of routes is on the 4th (2*2) line
# The middle term of that line (also the largest term) is the number of terms

number_of_grid = 20
nth_line = number_of_grid * 2

routes_line = Pascal().get_line(40)

print("Answer: ", max(routes_line))
