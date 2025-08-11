# O(log subx y)/O(1)
def check_power_v1(x, y):
    # The only power of 1 is itself
    if x <= 1:
        return y == 1 # covers x == 1 and x == 0

    # Repeatedly compute power of x
    pow = 1
    while pow < y:
        pow *= x

    # Check if power of x becomes y
    return pow == y


# -----------------------------------
# O(1)/O(1)
# Uses logarithms.
# Learn this somehow. Familiarize yourself with logarithms
import math

def is_power(x, y):
    result = math.log(y) / math.log(x)
    return result == math.floor(result)


if __name__ == "__main__":
    x = 2
    y = 128
    # print(check_power_v1(x, y))
    print(is_power(x, y))
