import math


# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


# Function to count primes in the GCD grid for a given N
def count_primes_in_gcd_grid(N):
    prime_count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if is_prime(math.gcd(i, j)):
                prime_count += 1
    return prime_count


# Main function to read input and produce output
def process_input_file(input_file, output_file):
    with open(input_file, 'r') as f:
        N_values = [int(line.strip()) for line in f.readlines()]

    with open(output_file, 'w') as f_out:
        for N in N_values:
            prime_count = count_primes_in_gcd_grid(N)
            print(prime_count)  # Output to screen
            f_out.write(f"{prime_count}\n")  # Output to file


# Example usage:
input_file = '1.txt'  # Modify with the actual input file
output_file = 'output.txt'
process_input_file(input_file, output_file)
