def deutsch_jozsa(f, n):
    num_tries = (2 ** (n - 1)) + 1
    prev_f_output = None
    for input_to_f in range(num_tries):
        f_output = f(input_to_f)
        if (prev_f_output is not None) and (prev_f_output ^ f_output):
            return 0  # balanced
        prev_f_output = f_output
    return 1  # constant


if __name__ == '__main__':
    def f1(input):
        return 0  # constant


    def f2(input):
        return (input & 1)  # returns lowest bit of input => balanced

    print('About to test deutsch_jozsa on f1, which is a constant function that always returns 0')
    result_f1 = deutsch_jozsa(f1, 5)
    expected_f1 = 1
    print('deutsch_jozsa works for f1? {}'.format(result_f1 == expected_f1))

    print('About to test deutsch_jozsa on f2, which is a balanced function that returns the lowest bit')
    result_f2 = deutsch_jozsa(f2, 7)
    expected_f2 = 0
    print('deutsch_jozsa works for f2? {}'.format(result_f2 == expected_f2))

