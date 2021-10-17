# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


primes = [2,3,5,7]
number = 10

while len(primes) != 10001:
    is_prime = True
    for num in primes:
        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
    
    number += 1

print(primes[-1])


