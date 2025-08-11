# USE THIS ONE
def multiply_table(num):
    length = 10

    for i in range(1, length + 1):
        print(f'{num} * {i} = {num * i}')
# ----------------------------------------

# Recursive
def recursive_table(num, i = 1):
    if i == 11:
        return
    print(f'{num} * {i} = {num * i}')
    i += 1
    recursive_table(num, i)

if __name__ == '__main__':
    num = 12
    # print(multiply_table(num))
    recursive_table(num)