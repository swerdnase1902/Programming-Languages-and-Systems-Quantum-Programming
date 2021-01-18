def deutsch_jozsa(f, n):
    num_tries = (2 ** n) + 1
    prev_f_output = None
    for input_to_f in range(num_tries):
        f_output = f(input_to_f)
        if (prev_f_output is not None) and (prev_f_output ^ f_output):
            return 0  # balanced
        prev_f_output = f_output
    return 1  # constant


if __name__ == '__main__':
    pass
