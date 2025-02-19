import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_primes>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer as the number of primes.")
        sys.exit(1)
    
    print_n_primes(n)