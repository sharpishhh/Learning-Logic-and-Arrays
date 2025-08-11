# Given a positive integer, find the sum of squares of the first n natural numbers

# USE THIS ONE
def better_sum(num):    # O(1) and O(1)
    return num * (num + 1) // 2
# ---------------------------------------------------------
def sum_naturals(num):  # O(n) time and O(1) space
    x = 1
    result = 0

    while x <= num:
        result += x
        x += 1
    return result
# ----------------------------------------------

if __name__ == '__main__':
    num = 4
    # print(sum_naturals(num))
    print(better_sum(num))