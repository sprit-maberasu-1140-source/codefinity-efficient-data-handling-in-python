def primes_up_to(n):
    if n < 2:
        return
    for num in range(2, n+1):
        is_prime=True
        limit=int(num**0.5) +1
        for i in range(2,limit):
            if num % i ==0:
                is_prime=False
                break
        if is_prime:
            yield num

# Sample usage
print(list(primes_up_to(10)))
print(list(primes_up_to(20)))
print(list(primes_up_to(1)))
