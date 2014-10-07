def triangle_num(n):
    _sum = 0
    for i in range(n + 1):
        _sum += i
    return _sum

def divisors(n):
    ret = []
    i = 1
    while i * i < n:
        if n % i == 0:
            ret.append(i)
            ret.append(n / i)
        i += 1
    return ret

n = 1
while True:
    nth_tri_num = triangle_num(n)
    if len(divisors(nth_tri_num)) > 500:
        print(nth_tri_num)
        break
    n += 1
