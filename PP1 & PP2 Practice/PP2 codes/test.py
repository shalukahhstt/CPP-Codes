# Function to compute the Hofstadter Female sequence
def hofstadter_f(n, F_values, M_values):
    if n in F_values:  # Use memoization to avoid recalculating
        return F_values[n]
    F_values[n] = n - hofstadter_m(hofstadter_f(n - 1, F_values, M_values), F_values, M_values)
    return F_values[n]


# Function to compute the Hofstadter Male sequence
def hofstadter_m(n, F_values, M_values):
    if n in M_values:  # Use memoization to avoid recalculating
        return M_values[n]
    M_values[n] = n - hofstadter_f(hofstadter_m(n - 1, F_values, M_values), F_values, M_values)
    print(M_values)
    return M_values[n]


def main(input_file):
    # Read the input file and get the indexes
    with open(input_file, 'r') as file:
        indexes = [int(line.strip()) for line in file.readlines()]

    # Initialize memoization dictionaries for F and M
    F_values = {0: 1}
    M_values = {0: 0}

    # Open the output file to write results
    with open('Output.txt', 'w') as output_file:
        # For each index in the file, compute F(n) and M(n)
        for n in indexes:
            F_n = hofstadter_f(n, F_values, M_values)
            M_n = hofstadter_m(n, F_values, M_values)

            # Prepare the result string
            result = f"{n}: F={F_n} M={M_n}"

            # Print result to screen
            print(result)

            # Write result to the output file
            output_file.write(result + '\n')


# Example usage:
input_file = '1.txt'
main(input_file)
