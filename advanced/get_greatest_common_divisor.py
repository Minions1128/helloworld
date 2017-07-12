def get_greatest_common_divisor_v1(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if (a%i==0) and (b%i==0):
            return i

def get_greatest_common_divisor_v2(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    return gcd(max(a, b), min(a, b))

def gcd(max_num, min_num):
    if max_num < min_num:
        raise
    if max_num % min_num == 0:
        return min_num
    else:
        return gcd(min_num, max_num%min_num)


print get_greatest_common_divisor_v1(5, 25)