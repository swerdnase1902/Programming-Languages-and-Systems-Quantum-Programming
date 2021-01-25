def simon(f, n):
    # n is bit length
    num_tries = 2**n
    output_to_input = [None]*num_tries  # the index is f(x) and the value is x
    for f_input in range(num_tries):
        f_output = f(f_input)
        if output_to_input[f_output] is not None:
            s = f_input ^ output_to_input[f_output]
            return s
        output_to_input[f_output] = f_input
    return None

if __name__ == '__main__':
    pass