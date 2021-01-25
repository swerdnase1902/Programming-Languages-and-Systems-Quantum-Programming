def simon(f, n):
    # n is bit length
    num_tries = 2 ** n
    # We use the output_to_input table to check if a specific output of f(x) has been seen before...
    output_to_input = [None] * num_tries  # the index is f(x) and the value is x
    for f_input in range(num_tries):
        f_output = f(f_input)
        if output_to_input[f_output] is not None:
            # Here, we found that f_output has been observed before
            s = f_input ^ output_to_input[f_output]
            return s
        output_to_input[f_output] = f_input
    return None


if __name__ == '__main__':
    def f1(x):
        # s = 0b101
        table = [0b000, 0b010, 0b001, 0b100, 0b010, 0b000, 0b100, 0b001]
        return table[x]


    print('About to test classical Simon solver on f1 with s=101')
    f1_expected_s = 0b101
    f1_calculated_s = simon(f1, 3)
    print('Expected to get s={} and actually got s={}'.format(bin(f1_expected_s), bin(f1_calculated_s)))
    print('Did the classical solver get the correct s? {}'.format(f1_expected_s == f1_calculated_s))
