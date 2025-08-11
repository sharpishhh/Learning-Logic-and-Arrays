# USE THIS ONE

def even_odd(num):
    if num % 2 == 0:
        return 'true'
    else:
        return 'false'
# ----------------------------------

# Bitwise Version
# Use this for even/odd situations
def efficient_even_odd(num):
    if (num & 1) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    num = 15
    print(even_odd(num))
    if efficient_even_odd(num):
        print('true')
    else:
        print('false')