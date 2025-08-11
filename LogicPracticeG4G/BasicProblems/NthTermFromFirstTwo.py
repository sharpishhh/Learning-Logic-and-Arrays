# Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively,
# the problem is to find the nth term of the series.
# USE THIS ONE
# O1/O1
def formula_nth_term(a1, a2, n):
    return a1 + (n - 1) * (a2 - a1) # start point + (length) * (step)
# ----------------------------------------
# On/O1
def naive_nth_term(a1, a2, n):
    step = a2 - a1
    nth_term = a1 # first number value they started with in the series

    for i in range(1, n): # range for the index of the series
        nth_term += step # move forward by the step range
    return nth_term # when the nth index is reached return the nth_term(value at the nth index)



if __name__ == '__main__':
    print(naive_nth_term(2, 3, 4))