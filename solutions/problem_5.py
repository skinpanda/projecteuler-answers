# Title: Smallest multiple

# LCM(A, B) = (A*B)/GCD(A, B)
# To find GCD(A, B), use Euclidean Algorithm
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


def lcm(x, y):
  return ((x*y)//gcd(x, y))


def gcd(x, y):
  while x*y:
    x, y = y, x % y
  return x+y


# LCM(A, B, C) = LCM(LCM(A, B), C) ..

SmallestMultiple = 1
for i in range(11, 21):
  SmallestMultiple = lcm(SmallestMultiple, i)

print("Answer: ", SmallestMultiple)
