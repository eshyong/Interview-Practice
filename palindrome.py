def is_palindrome(number):
    chars = list(str(number))
    length = len(chars)

    # Iterate from 0 to n/2.
    i = 0
    while i < length/2:
        if chars[i] != chars[length-i-1]:
            return False
        i += 1
    return True

biggest = 0
limit = 999
for i in reversed(range(limit)):
    for j in reversed(range(limit)):
        n = i*j
        print(n)
        if is_palindrome(n) and n > biggest:
            biggest = n
            break

print(biggest)
