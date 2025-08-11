# USE THIS ONE
def tuple_swap(a, b):
    a, b = b, a
    return a, b
# ---------------------------------

def naive_swap_two(a, b):   # O(1), O(1)
    c = a
    a = b
    b = c
    return a, b

def expected_swap1(a, b): # O(1), O(1)
    # Arithmetic
    a = a + b
    b = a - b
    a = a - b
    return a, b

def expected_swap2(a, b):   # O(1), O(1)
    # Bitwise XOR
    a = a ^ b # a holds result of a ^ b
    b = a ^ b # gets you the original value of a (b = (a^b)^b = a
    a = a ^ b # gets the original value of b (a = (a^b)^a=b
    return a, b
# -------------------------------------


if __name__ == '__main__':
    a = 2
    b = 3
    print(naive_swap_two(a, b))
    print(expected_swap1(a, b))
    print(expected_swap2(a, b))
    print(tuple_swap(a, b))