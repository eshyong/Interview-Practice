bignum = 2 ** 1000
# print(list(str(bignum)))
_sum = 0
for i in list(str(bignum)):
    _sum += int(i)

print(_sum)

