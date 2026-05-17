def infinite_multiples(k):
    # Your code here
    pass
    current = k
    while True:
        yield current
        current += k

gen = infinite_multiples(3)
for _ in range(5):
    print(next(gen))
