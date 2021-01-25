def grover(f, n):
    # loop through all possible inputs and see if output is 1
    num_tries = 2 ** n
    for f_input in range(num_tries):
        if f(f_input) == 1:
            return 1
    return 0


if __name__ == '__main__':
    def f1(x):
        return 0


    def f2(x):
        return int(x == 0b1011)


    print('About to test classical grover solver on f1 which always outputs 0')
    f1_expected = 0
    f1_calculated = grover(f1, 4)
    print('Expected to get {} and actually got {}'.format(f1_expected, f1_calculated))
    print('Did the classical solver get the correct answer? {}'.format(f1_expected == f1_calculated))

    print('About to test classical grover solver on f2 which outputs 1 only when x=0b1011')
    f2_expected = 1
    f2_calculated = grover(f2, 4)
    print('Expected to get {} and actually got {}'.format(f2_expected, f2_calculated))
    print('Did the classical solver get the correct answer? {}'.format(f2_expected == f2_calculated))