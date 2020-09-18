# calculator.py

def sum(m,n):
    tot = m
    for i in (0, n):
        if (n > 0):
            tot += 1
        else:
            tot -= 1
    return tot


def divide(m,n):
    if n == 0:
        # no!
        raise ZeroDivisionError
    
    isNegative = m<0 and n>0 or m>0 and n<0

    m = abs(m)
    n = abs(n)
    result = 0
    while ((m - n) >= 0):
        result = result + 1
        m -= n

    return -result if isNegative else result