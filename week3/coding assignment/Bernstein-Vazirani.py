def bernstein_vazirani(f, n):
    b = f(0)
    a = 0
    input_to_f = 1
    for shift in range(n):
        a_bit = (f(input_to_f)) ^ b  # Since f = a*x + b, we have f + b = a*x
        a_bit <<= shift
        input_to_f <<= 1
        a = a | a_bit
    return a, b


if __name__ == '__main__':
    def f1(input):
        a = 0b000101  # a = 5
        b = 0b1  # b = 1
        return (bin(a & input).count("1") & 1) ^ b  # performs a*x + b


    def f2(input):
        a = 0b111011
        b = 0b0
        return (bin(a & input).count("1") & 1) ^ b


    print('About to test bernstein_vazirani on f1 (a=0b000101, b=1)...')
    result_f1 = bernstein_vazirani(f1, 6)
    expected_f1 = (0b000101, 0b1)
    print("bernstein_vazirani works for f1 (a=0b000101, b=1)? {}".format(result_f1 == expected_f1))

    print('About to test bernstein_vazirani on f2 (a=0b111011, b=0)...')
    result_f2 = bernstein_vazirani(f2, 6)
    expected_f2 = (0b111011, 0b0)
    print("bernstein_vazirani works for f2 (a=0b111011, b=0)? {}".format(result_f2 == expected_f2))
