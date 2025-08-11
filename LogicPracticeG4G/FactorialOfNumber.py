def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = n
    while n >= 2:
         result *= n-1
         n -= 1
         # print(n, result)
    return result

def factorialG4G(n):
    res = 1

    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    n = 5
    print(factorial(n))
    print(factorialG4G(n))