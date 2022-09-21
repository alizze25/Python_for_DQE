# 1 Generate 100 random numbers between 0 and 1000
import random
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)

# 2 sort list from min to max
l = randomlist
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
            print(l)

# 3 calculate average for even and odd numbers

from functools import reduce

ev = randomlist
even = [i for i in ev if i % 2 == 0]  # only even numbers
print(sum(even) / len(even))  # Divide the sum of even numbers by their number

from functools import reduce

b = randomlist
odd = [i for i in b if i % 2 != 0]  # only odd numbers
print(sum(odd) / len(odd)) # Divide the sum of odd numbers by their numbers



