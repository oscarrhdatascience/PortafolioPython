def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    return [num for num in range(start, end+1) if is_prime(num)]

print(find_primes_in_range(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
