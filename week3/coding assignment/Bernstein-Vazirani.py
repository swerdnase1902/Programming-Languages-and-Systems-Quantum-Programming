def bernstein_vazirani(f, n):
    b = f(0)
    a = 0
    input_to_f = 1
    for shift in range(n):
        a <<= 1
        a_bit = (f(input_to_f)) ^ b
        input_to_f <<= 1
        a = a | a_bit
    return a, b

if __name__ == '__main__':
    pass
