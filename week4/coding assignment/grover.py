def grover(f, n):
    num_tries = 2 ** n
    for f_input in range(num_tries):
        if f(f_input) == 1:
            return 1
    return 0

if __name__ == '__main__':
    pass