# Title: Sum square difference

# Use list comprehension
sumofsquares = sum([x**2 for x in range(1, 101)])
squareofsums = sum(range(1, 101))**2

print("Answer: ", squareofsums - sumofsquares)
