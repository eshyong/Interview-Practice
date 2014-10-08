import math
import random
import sys

def smallest_distance(small_list, large_list):
    i, j = 0, 0
    min_i, min_j = 0, 0
    min_dist = sys.maxint
    while i < len(small_list) and j < len(small_list):
        distance = int(math.fabs(small_list[i] - large_list[j]))
        if min_dist > distance:
            min_dist = distance
            min_i = i
            min_j = j
        if small_list[i] > large_list[j]:
            j += 1
        elif small_list[i] < large_list[j]:
            # Only increment i if we find a larger item in the bigger list. We know that 
            # both lists are sorted, and that large_list[j+1] >= large_list[j], therefore
            # large_list[j+1] - small_list[i] >= large_list[j] - small_list[i], so we
            # continue in the small list. This also ensures that the algorithm terminates early.
            i += 1
        else:
            # Early return, means we have a duplicate.
            return (small_list[min_i], large_list[min_j], 0)

    # Return a tuple.
    return (small_list[min_i], large_list[min_j], min_dist)

small_list = []
large_list = []

small = 10
large = 1000
for i in range(small):
    small_list.append(random.randint(1, 100000))

for i in range(large):
    large_list.append(random.randint(1, 100000))

small_list = sorted(small_list)
large_list = sorted(large_list)

print(small_list)
print(large_list)

print(smallest_distance(small_list, large_list))
