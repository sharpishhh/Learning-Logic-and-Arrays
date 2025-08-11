# Given a number n, find the sum of its digits.

# USE THIS ONE
# Olog10n/O1
def digit_extract(n):
    total = 0
    while n != 0:
        last = n % 10
        total += last
        n //= 10
    return total




# -------------------------------------------
def sumofDig(n):
    # Convert to string
    s = str(n)
    sum = 0

    # Loop through each char, convert to digit, and add to sum
    for ch in s:
        sum += int(ch)
    return sum
# -------------------------------------------
# O(log10n)/O(log10n)
def recursion_sum(n):
    if n == 0:
        return 0

    return n % 10 + recursion_sum(n // 10)
# --------------------------------------------


if __name__ == '__main__':
    n = 687
    print(digit_extract(n))
    print(recursion_sum(n))
    print(sumofDig(n))