# Given two integers n and m (m != 0); Find num closest to n and divisible by m. IF there
# is more than one such num, output the one having max absolute value

# USE THIS ONE
# O(1) Time and O(1) Space
def closest_fast(n, m):
    # Multiplying the quotient back yields the greatest multiple of m that
    # does not exceed n(when m is positive)
    q = n//m

    # 1st possible closest num
    n1 = m * q

    # 2nd possible closest num
    if ((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    # if true, the n1 is the required closest num
    if (abs(n - n1) < abs(n - n2)):
        return n1

    # else n2 is the required closest num
    return n2


# ------------------------------------
# O(m) Time and O(1) Space
def naive_closest_num(n, m):
    closest = 0
    min_diff = float('inf')

    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            diff = abs(n - i)

            if diff < min_diff or \
                    (diff == min_diff and abs(i) > abs(closest)):
                closest = i
                min_diff = diff
    return closest

if __name__ == '__main__':
    n = 13
    m = 4
    print(naive_closest_num(n, m))
    print(closest_fast(n, m))