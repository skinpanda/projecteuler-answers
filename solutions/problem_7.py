from itertools import count
import math
import time

p = 2
s = time.time()
for i in count(5, 2):
  test = True
  for j in range(2, int(math.sqrt(i))+1):
    if i%j == 0:
      test = False
      break
  
  if test:
    p += 1
  if p == 10001:
    break
  
print(i)
print(time.time()-s)  
