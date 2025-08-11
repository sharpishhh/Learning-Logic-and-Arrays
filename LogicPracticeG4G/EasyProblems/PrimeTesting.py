# O(n)/O(1)
def prime_v1(n):

    if n <= 1:
        return False

    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True

# ----------------------------------
# Optimized Version
# O(sqrt n)/O(1) ???
import math

def is_prime(n):

    # Corner Case
    if n <= 1:
        return False

    # Check from 2 to square root of n
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = 11
    print(prime_v1(n))
    print(is_prime(n))