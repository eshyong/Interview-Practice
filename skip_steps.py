def ways_to_skip(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    else:
        one = [1] + [item for item in ways_to_skip(n - 1)]
        two = [2] + [item for item in ways_to_skip(n - 2)]
        three = [3] + [item for item in ways_to_skip(n - 3)]
        return [one, two, three]

print(ways_to_skip(1))
print(ways_to_skip(2))
print(ways_to_skip(3))
print(ways_to_skip(4))
print(ways_to_skip(5))
print(ways_to_skip(6))
