def number_generator(n):
    for i in range(1,n+1):
        yield i

def square_generator(n):
     for i in range(1,n+1):
         yield i*i

def chained_generator(n):
    yield from number_generator(n)
    yield from square_generator(n)

# Example usage:
for value in chained_generator(3):
    print(value)
