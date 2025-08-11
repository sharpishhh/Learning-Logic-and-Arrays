# Given an integer, find the reverse of its digits

# USE THIS ONE
# Digit by Digit
# O(log n)/O(1)
def reverse_dig1(n):
    result = 0
    while n != 0:
        last = n % 10
        result = result * 10 + last
        n //= 10
    return result




# ----------------------------------
# Recursion
# O(log n)/O(log n)
# I don't understand this one yet. Review later
def recursive_reverse(n, revNum, basePos):
    if n > 0:
        recursive_reverse(n // 10, revNum, basePos)
        revNum[0] += (n % 10) * basePos[0]
        basePos[0] *= 10
        return revNum[0]
# -----------------------------------
# String
# O(log n)/O(1)
def string_reverse(n):
    s = str(n)
    s = list(s)
    s.reverse()
    s = ''.join(s)
    n = int(s)
    return n

if __name__ == '__main__':
    n = 122
    revNum = [0]
    basePos = [1]
    # print(recursive_reverse(n, revNum, basePos))
    print(reverse_dig1(n))
    # print(string_reverse(n))